# type: ignore

import asyncio
import websockets
import json
import mesa

# --- MESA 3.0+ SIN "TIME" MODULE ---

class MyAgent(mesa.Agent):
    """
    En Mesa 3.0+, el agente debe recibir el modelo en su constructor.
    'self.pos' y 'self.unique_id' son gestionados internamente por la clase base.
    """
    def __init__(self, unique_id, model):
        super().__init__(model)
        self.unique_id = unique_id
        # No necesitamos nada más, la posición se asigna al usar grid.place_agent

class MyModel(mesa.Model):
    def __init__(self, width=100, height=100):
        super().__init__()
        # Inicializamos el Grid (MultiGrid permite varios agentes en la misma celda)
        self.grid = mesa.space.MultiGrid(width, height, torus=False)
        
        # YA NO USAMOS self.schedule = RandomActivation(self)
        # Mesa 3.0+ gestiona los agentes nativamente en 'self.agents'
        
        # Mantenemos un diccionario auxiliar para acceso rápido O(1) por ID
        # ya que el WebSocket envía IDs específicos.
        self.agents_dict = {} 

    def add_agent(self, agent_id, x, y):
        if agent_id not in self.agents_dict:
            # Instanciamos el agente pasando el modelo (self)
            a = MyAgent(agent_id, self)
            
            # Al crear el agente con 'self', Mesa 3.0 lo añade automáticamente a self.agents
            # Nosotros lo guardamos en nuestro dict para control manual
            self.agents_dict[agent_id] = a
            
            # Colocar en el grid
            self.grid.place_agent(a, (x, y))

    def move_agent(self, agent_id, x, y):
        """Mueve un agente existente a una nueva coordenada."""
        a = self.agents_dict.get(agent_id)
        if a:
            self.grid.move_agent(a, (x, y))

    def remove_agent(self, agent_id):
        """Elimina el agente del grid y del registro."""
        a = self.agents_dict.pop(agent_id, None)
        if a:
            self.grid.remove_agent(a)
            a.remove() # Método nativo de Mesa 3.0 para sacarlo de self.agents

    def serialize_grid(self):
        """
        Serializa el estado para enviar a Unity.
        CORRECCIÓN CRÍTICA: coord_iter() en Mesa 3+ devuelve (cell_content, (x, y))
        """
        data = []
        for cell_content, (x, y) in self.grid.coord_iter():
            for agent in cell_content:
                data.append({
                    "id": agent.unique_id,
                    "x": x,
                    "y": y
                })
        return data

# --- LÓGICA WEBSOCKET (Idéntica, pero usando el modelo actualizado) ---

connected_clients = set()
model = MyModel(10, 10)

async def receive_message(message):
    try:
        data = json.loads(message)
        if data.get("type") == "update":
            for ag in data["agents"]:
                ag_id = ag["id"]
                x = ag["x"]
                y = ag["y"]

                # Validación de límites del Grid
                if 0 <= x < model.grid.width and 0 <= y < model.grid.height:
                    if ag_id not in model.agents_dict:
                        model.add_agent(ag_id, x, y)
                    else:
                        model.move_agent(ag_id, x, y)
    except Exception as e:
        print(f"Error procesando data: {e}")

async def send_world_state():
    if not connected_clients:
        return
    
    state = {
        "type": "update",
        "agents": model.serialize_grid()
    }
    msg = json.dumps(state)
    
    # Broadcast a todos los clientes
    websockets.broadcast(connected_clients, msg)

async def handler(ws):
    connected_clients.add(ws)
    print("Unity conectado.")
    try:
        async for message in ws:
            await receive_message(message)
            await send_world_state()
    except websockets.ConnectionClosed:
        print("Unity desconectado.")
    finally:
        connected_clients.remove(ws)

if __name__ == "__main__":
    async def main():
        async with websockets.serve(handler, "localhost", 8765):
            print("Servidor Mesa (v3.0+ No-Time) listo en ws://localhost:8765")
            await asyncio.get_running_loop().create_future()

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass