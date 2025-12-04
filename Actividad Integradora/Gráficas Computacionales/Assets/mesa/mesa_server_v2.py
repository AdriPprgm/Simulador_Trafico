# type: ignore
import mesa
from mesa.discrete_space import CellAgent, OrthogonalVonNeumannGrid
from collections import deque
import asyncio
import websockets
import json
import diccionario_movimientos

#type: ignore
#Funcion "breadth_first_search" que llamaremos para calcular la ruta que debe tomar el agente "Carro" para llegar de un punto a otro
# Esta misma funcion se llamara nuevamente en caso de que el agente Carro encuentre un obstaculo.

def breadth_first_search(start: tuple, goal: tuple, grid: OrthogonalVonNeumannGrid) -> list[tuple]:
    queue: deque[tuple] = deque()
    visited: set[tuple] = set()
    parent: dict[tuple, tuple] = {}

    queue.append(start)
    visited.add(start)

    while queue:
        current: tuple = queue.popleft()
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.pop(-1)
            return path[::-1]

        cell = grid[current].coordinate

        # Validar que cell esté dentro del rango del diccionario
        dict_x = cell[0] + 1
        dict_y = cell[1] + 1

        if dict_x not in diccionario_movimientos.adjusted_movement_map:
            continue
        if dict_y not in diccionario_movimientos.adjusted_movement_map[dict_x]:
            continue

        neighbors = diccionario_movimientos.adjusted_movement_map[dict_x][dict_y]

        for i in neighbors:
            cell_pos = (i[0] - 1, i[1] - 1)

            # Validar que cell_pos esté dentro del grid (0-47)
            if (cell_pos[0] < 0 or cell_pos[0] >= 48 or
                cell_pos[1] < 0 or cell_pos[1] >= 48):
                continue

            if cell_pos not in visited:
                neighbor_cell = grid[cell_pos]
                has_car = any(isinstance(agent, Carro) for agent in neighbor_cell.agents)
                is_park = any(isinstance(agent, AgenteCalle) and agent.isEstacionamiento for agent in neighbor_cell.agents)
                if not has_car:
                    visited.add(cell_pos)
                    parent[cell_pos] = current
                    queue.append(cell_pos)
                elif has_car:
                    if is_park:
                        visited.add(cell_pos)
                        parent[cell_pos] = current
                        queue.append(cell_pos)
    return []

# Clase "AgenteCalle" que tenga valores de dirección asociados, para marcar la circulación.

class AgenteCalle(CellAgent):
    def __init__(self, model, cell):
        super().__init__(model)
        self.cell = cell
        self.isBuilding = False
        self.isEstacionamiento = False

    def step(self):
        pass

# Agente "Semaforo"

class Semaforo1(CellAgent):
    def __init__(self, model, cell):
        super().__init__(model)
        self.cell = cell
        self.avanza = False
        self.contador = 0

    def cambair_estado(self):
        self.avanza = not self.avanza

    def step(self):
        self.contador += 1
        if self.contador >= 5:
            self.cambair_estado()
            self.contador = 0

class Semaforo2(CellAgent):
    def __init__(self, model, cell):
        super().__init__(model)
        self.cell = cell
        self.avanza = True
        self.contador = 0

    def cambair_estado(self):
        self.avanza = not self.avanza

    def step(self):
        self.contador += 1
        if self.contador >= 5:
            self.cambair_estado()
            self.contador = 0

# Agente "Camion"

# Agente "Carro"

class Carro(CellAgent):
    def __init__(self, model, cell):
        super().__init__(model)
        self.cell = cell
        self.destino = model.random.choice(model.estacionamientos_cells).coordinate
        while self.destino == self.cell.coordinate:
            self.destino = model.random.choice(model.estacionamientos_cells).coordinate
        self.estacionado = False
        self.ruta = []

    def calcular_ruta(self):
        self.ruta = breadth_first_search(self.cell.coordinate, self.destino, self.model.grid)

    def puede_avanzar(self):
        siguiente_celda = self.obtener_siguiente()
        if not siguiente_celda:
            return False
        estado_estacionamiento = None
        for agente in siguiente_celda.agents:
            if isinstance(agente, AgenteCalle):
                estado_estacionamiento = agente
            if isinstance(agente, Carro) and not estado_estacionamiento.isEstacionamiento:
                return False
            if isinstance(agente, (Semaforo1, Semaforo2)):
                if not agente.avanza:
                    return False
        return True

    def avanzar(self):
        siguiente_celda = self.obtener_siguiente()
        if siguiente_celda:
            self.cell = siguiente_celda
            self.ruta.pop(0)

    def detenerse(self):
        pass

    def obtener_siguiente(self):
        if not self.ruta:
            return None
        siguiente_pos = self.ruta[0]
        siguiente_celda = self.model.grid[siguiente_pos]
        return siguiente_celda

    def cambiar_carril(self):
        x = self.puede_cambiar()
        if x:
            self.ruta = x

    def puede_cambiar(self):
        siguiente_celda = self.obtener_siguiente()
        if not siguiente_celda:
            return False
        for agente in siguiente_celda.agents:
            if isinstance(agente, (Semaforo1, Semaforo2)):
                return False
        return breadth_first_search(self.cell.coordinate, self.destino, self.model.grid)

    def llego_destino(self):
        return self.cell.coordinate == self.destino

    def estacionarse(self):
        if not self.estacionado:
            self.estacionado = True
        else:
            pass

    def step(self):
        if not self.ruta:
            self.calcular_ruta()
            if not self.ruta:
                self.destino = self.model.random.choice(self.model.estacionamientos_cells).coordinate
                while self.destino == self.cell.coordinate:
                    self.destino = self.model.random.choice(self.model.estacionamientos_cells).coordinate
        if not self.estacionado:
            if self.puede_avanzar():
                self.avanzar()
            else:
                self.cambiar_carril()
        if self.llego_destino():
            self.estacionarse()
        if self.estacionado:
            pass

# Modelo

class TrafficModel(mesa.Model):
    def __init__(self, n):
        super().__init__()
        self.num_cars = n
        self.grid = OrthogonalVonNeumannGrid((48, 48), torus = False, capacity = 500, random = self.random)
        self.estacionamientos_cells = []

        for x in range(width):
            for y in range(height):
                cell = self.grid[(x, y)]
                calle = AgenteCalle(self, cell)

                #Set Semaforos1 (sumamos +12 a todas las coordenadas)
                if (x == 33 and (y == 16 or y == 17 or y == 22 or y == 23) or
                    x == 14 and (y == 16 or y == 17 or y == 20 or y == 21) or
                    x == 19 and (y == 34 or y == 35) or
                    x == 27 and (y == 34 or y == 35) or
                    x == 24 and (y == 12 or y == 13)):
                    semaforo1 = Semaforo1(self, cell)

                #Set Semaforos2 (sumamos +12 a todas las coordenadas)
                if (y == 15 and (x == 12 or x == 13) or
                    y == 19 and (x == 12 or x == 13) or
                    y == 14 and (x == 22 or x == 23) or
                    y == 18 and (x == 34 or x == 35) or
                    y == 24 and (x == 34 or x == 35) or
                    y == 33 and (x == 20 or x == 21 or x == 28 or x == 29)):
                    semaforo2 = Semaforo2(self, cell)

                #Set Buildings (sumamos +12 a todas las coordenadas)
                if ((13 < x < 16) and (13 < y < 16) or
                    (13 < x < 16) and (17 < y < 20) or
                    (13 < x < 16) and (23 < y < 28) or
                    (13 < x < 20) and (29 < y < 34) or
                    (17 < x < 20) and (13 < y < 16) or
                    (17 < x < 20) and (17 < y < 20) or
                    (17 < x < 20) and (23 < y < 28) or
                    (23 < x < 34) and (13 < y < 16) or
                    (23 < x < 34) and (17 < y < 20) or
                    (23 < x < 28) and (23 < y < 27) or
                    (23 < x < 28) and (28 < y < 34) or
                    (29 < x < 34) and (23 < y < 34) or
                    (20 < x < 23) and (20 < y < 23)):
                    calle.isBuilding = True

                #Set Estacionamiento (sumamos +12 a todas las coordenadas)
                if ((x == 15 and y == 15) or  # Estacionamiento 13
                    (x == 19 and y == 18) or  # Estacionamiento 17
                    (x == 15 and y == 24) or  # Estacionamiento 12
                    (x == 18 and y == 27) or  # Estacionamiento 15
                    (x == 18 and y == 30) or  # Estacionamiento 16
                    (x == 16 and y == 33) or  # Estacionamiento 14
                    (x == 25 and y == 15) or  # Estacionamiento 2
                    (x == 26 and y == 18) or  # Estacionamiento 5
                    (x == 26 and y == 26) or  # Estacionamiento 3
                    (x == 24 and y == 30) or  # Estacionamiento 1
                    (x == 26 and y == 33) or  # Estacionamiento 4
                    (x == 32 and y == 14) or  # Estacionamiento 10
                    (x == 31 and y == 19) or  # Estacionamiento 8
                    (x == 31 and y == 24) or  # Estacionamiento 7
                    (x == 33 and y == 28) or  # Estacionamiento 11
                    (x == 30 and y == 31) or  # Estacionamiento 6
                    (x == 32 and y == 33)):  # Estacionamiento 9
                    calle.isEstacionamiento = True
                    self.estacionamientos_cells.append(self.grid[(x, y)])

        agents = Carro.create_agents(
            self,
            self.num_cars,
            self.random.choices(self.estacionamientos_cells, k=self.num_cars),

        )
    def step(self):
        for agent in list(self.agents):
            agent.step()

# --- LÓGICA WEBSOCKET ---

connected_clients = set()
width = 48
height = 48
model = TrafficModel(50)

def serialize_agents():
    """Serializa todos los agentes del modelo para enviar a Unity"""
    agents_data = []

    for agent in model.agents:
        agent_dict = {
            "id": agent.unique_id,
            "x": agent.cell.coordinate[0],
            "y": agent.cell.coordinate[1],
            "type": type(agent).__name__
        }

        # Agregar información específica según el tipo de agente
        if isinstance(agent, Carro):
            agent_dict["estacionado"] = agent.estacionado
            agent_dict["destino_x"] = agent.destino[0]
            agent_dict["destino_y"] = agent.destino[1]
        elif isinstance(agent, (Semaforo1, Semaforo2)):
            agent_dict["avanza"] = agent.avanza
        elif isinstance(agent, AgenteCalle):
            agent_dict["isBuilding"] = agent.isBuilding
            agent_dict["isEstacionamiento"] = agent.isEstacionamiento

        agents_data.append(agent_dict)

    return agents_data

async def send_world_state():
    """Envía el estado actual del mundo a todos los clientes conectados"""
    if not connected_clients:
        return

    state = {
        "type": "update",
        "step": model.steps,
        "agents": serialize_agents()
    }
    msg = json.dumps(state)

    # Broadcast a todos los clientes
    websockets.broadcast(connected_clients, msg)

async def simulation_loop():
    """Loop principal de la simulación"""
    while True:
        model.step()
        await send_world_state()
        await asyncio.sleep(1)  # Delay entre pasos (ajustable)

async def handler(ws):
    """Maneja las conexiones WebSocket"""
    connected_clients.add(ws)
    print(f"Unity conectado. Total clientes: {len(connected_clients)}")

    try:
        # Enviar estado inicial
        await send_world_state()

        # Mantener la conexión abierta
        async for message in ws:
            # Procesar comandos desde Unity si es necesario
            try:
                data = json.loads(message)
                if data.get("type") == "pause":
                    print("Simulación pausada")
                elif data.get("type") == "resume":
                    print("Simulación reanudada")
            except json.JSONDecodeError:
                print(f"Mensaje inválido recibido: {message}")

    except websockets.ConnectionClosed:
        print("Unity desconectado.")
    finally:
        connected_clients.remove(ws)
        print(f"Clientes restantes: {len(connected_clients)}")

if __name__ == "__main__":
    async def main():
        # Iniciar servidor WebSocket
        server = await websockets.serve(handler, "localhost", 8765)
        print("Servidor Mesa listo en ws://localhost:8765")
        print(f"Modelo inicializado con {model.num_cars} carros")
        print(f"Grid: {width}x{height}")

        # Iniciar loop de simulación
        asyncio.create_task(simulation_loop())

        # Mantener el servidor corriendo
        await asyncio.get_running_loop().create_future()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServidor detenido.")