# type: ignore
import numpy as np

import pandas as pd

import seaborn as sns

import mesa

from mesa.discrete_space import CellAgent, OrthogonalVonNeumannGrid

import random

import time

from matplotlib.colors import ListedColormap

from collections import deque

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
                has_truck = any(isinstance(agent, Camion) for agent in neighbor_cell.agents)
                has_car = any(isinstance(agent, Carro) for agent in neighbor_cell.agents)
                is_park = any(isinstance(agent, AgenteCalle) and agent.isEstacionamiento for agent in neighbor_cell.agents)
                if is_park or (not has_car and not has_truck):
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
        self.tiempo_verde = 4
        self.tiempo_rojo = 8

    def cambiar_estado(self):
        self.avanza = not self.avanza

    def step(self):
        self.contador += 1
        if self.avanza:
            if self.contador >= self.tiempo_verde:
                self.cambiar_estado()
                self.contador = 0
        else:
            if self.contador >= self.tiempo_rojo:
                self.cambiar_estado()
                self.contador = 0

class Semaforo2(CellAgent):
    def __init__(self, model, cell):     
        super().__init__(model)
        self.cell = cell
        self.avanza = True
        self.contador = -2
        self.tiempo_verde = 4
        self.tiempo_rojo = 8

    def cambiar_estado(self):
        self.avanza = not self.avanza

    def step(self):
        self.contador += 1
        if self.avanza:
            if self.contador >= self.tiempo_verde:
                self.cambiar_estado()
                self.contador = 0
        else:
            if self.contador >= self.tiempo_rojo:
                self.cambiar_estado()
                self.contador = 0

# Agente "Camion"

class Camion(CellAgent):
    def __init__(self, model):
        super().__init__(model)
        self.cell = model.grid[(18, 27)]
        self.ruta = []
        self.numero_parada = 0
        self.siguiente_parada = model.paradas_camion_cells[self.numero_parada].coordinate
        self.contador_espera = 0
        self.estacionado = False

    def calcular_ruta(self):
        self.ruta = breadth_first_search(self.cell.coordinate, self.siguiente_parada, self.model.grid)
    
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
            if isinstance(agente,Camion) and not estado_estacionamiento.isEstacionamiento:
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
        return breadth_first_search(self.cell.coordinate, self.siguiente_parada, self.model.grid)

    def llego_destino(self):
        return self.cell.coordinate == self.siguiente_parada

    def estacionarse(self):
        if not self.estacionado:
            self.estacionado = True
        else:
            pass

    def step(self):
        if not self.ruta:
            self.calcular_ruta()
        if not self.estacionado:
            if self.puede_avanzar():
                self.avanzar()
            else:
                self.cambiar_carril()
        if self.llego_destino():
            if self.contador_espera < 5:
                self.contador_espera += 1
                pass
            else:
                self.contador_espera = 0
                if self.numero_parada < len(model.paradas_camion_cells) - 1:
                    self.numero_parada += 1
                    self.siguiente_parada = model.paradas_camion_cells[self.numero_parada].coordinate
                    self.calcular_ruta()
                else:
                    self.numero_parada = 0
                    self.siguiente_parada = model.paradas_camion_cells[self.numero_parada].coordinate
                    self.calcular_ruta()
        if self.estacionado:
            pass


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
            if isinstance(agente,Camion) and not estado_estacionamiento.isEstacionamiento:
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
        self.paradas_camion_cells = [self.grid[(25, 34)],
                                     self.grid[(34, 25)],
                                     self.grid[(25, 13)],
                                     self.grid[(13, 26)]]

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

                #Set Buildings
                dict_x = x + 1
                dict_y = y + 1
                if dict_x in diccionario_movimientos.adjusted_movement_map:
                    if dict_y in diccionario_movimientos.adjusted_movement_map[dict_x]:
                        if not diccionario_movimientos.adjusted_movement_map[dict_x][dict_y]:
                            calle.isBuilding = True
                    else:
                        calle.isBuilding = True
                else:
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
                    (x == 32 and y == 33) or  # Estacionamiento 9
                    
                    #Nuevos estacionemientos
                    (x == 9 and y == 2) or   
                    (x == 2 and y == 2) or   
                    (x == 45 and y == 2) or   
                    (x == 2 and y == 15) or   
                    (x == 2 and y == 19) or   
                    (x == 6 and y == 43) or   
                    (x == 36 and y == 38) or  
                    (x == 44 and y == 18) or  
                    (x == 35 and y == 2)):  
                    
                    calle.isEstacionamiento = True
                    self.estacionamientos_cells.append(self.grid[(x, y)])

        agents = Carro.create_agents(
            self,
            self.num_cars,
            self.random.choices(self.estacionamientos_cells, k=self.num_cars),

        )
        camiones = Camion.create_agents(
            self,
            3
        )
    def step(self):
        for agent in list(self.agents):
            agent.step()

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    print("Testing Carro agents with visualization...")
    
    width = 48
    height = 48
    model = TrafficModel(50)
    
    carros = [agent for agent in model.agents if isinstance(agent, Carro)]
    camiones = [agent for agent in model.agents if isinstance(agent, Camion)]
    
    print(f"Total cars: {len(carros)}")
    for i, carro in enumerate(carros):
        print(f"Car {i+1} - Starting position: {carro.cell.coordinate}, Destination: {carro.destino}")
    
    plt.ion()
    
    fig, ax = plt.subplots(figsize=(12, 12))
    
    def get_grid_state():
        """Create a grid showing car positions"""
        grid_state = np.zeros((height, width))
        
        # Marcar buildings y estacionamientos
        for cell in model.grid.all_cells:
            calle_agents = [agent for agent in cell.agents if isinstance(agent, AgenteCalle)]
            if calle_agents and calle_agents[0].isBuilding:
                x, y = cell.coordinate
                grid_state[y, x] = 4  # Buildings
            if calle_agents and calle_agents[0].isEstacionamiento:
                x, y = cell.coordinate
                grid_state[y, x] = 8 # Estacionamientos
        
        #Marcar Semaforos
        for cell in model.grid.all_cells:
            semaforo_agent = [agent for agent in cell.agents if isinstance(agent, Semaforo1) or isinstance(agent, Semaforo2)]
            if semaforo_agent and semaforo_agent[0].avanza:
                x, y = cell.coordinate
                grid_state[y, x] = 5
            elif semaforo_agent and not semaforo_agent[0].avanza:
                x, y = cell.coordinate
                grid_state[y, x] = 3
        
        # Marcar destino de todos los coches
        for carro in carros:
            if not carro.estacionado:
                dest_x, dest_y = carro.destino
                grid_state[dest_y, dest_x] = 6 
        
        # Marcar todas las posiciones de coches
        for carro in carros:
            if not carro.estacionado:
                x, y = carro.cell.coordinate
                grid_state[y, x] = 2
        
        for parada in model.paradas_camion_cells:
            x, y = parada.coordinate
            grid_state[y, x] = 9
        
        for camion in camiones:
            x, y = camion.cell.coordinate
            grid_state[y, x] = 7
        
        return grid_state
    
    colors = ['white', 'lightblue', 'blue', 'red', 'grey', 'green', 'black', 'orange', 'yellow', 'pink']
    cmap = ListedColormap(colors)
    
    step_counter = 0
    
    while any(not carro.estacionado for carro in carros) or any(not camion.estacionado for camion in camiones):
        model.step()
        step_counter += 1
        
        grid_state = get_grid_state()
        
        ax.clear()

        sns.heatmap(grid_state, cmap=cmap, vmin=0, vmax=9,
                   square=True, linewidths=0.5, linecolor='gray',
                   cbar=False, ax=ax, annot=False)
        
        # Dibujar camellones
        ax.plot([22, 22], [14, 20], color='black', linewidth=3)
        ax.plot([22, 22], [24, 34], color='black', linewidth=3)
        ax.plot([14, 20], [22, 22], color='black', linewidth=3)
        ax.plot([24, 34], [22, 22], color='black', linewidth=3)
        
        active_cars = sum(1 for carro in carros if not carro.estacionado)
        ax.set_title(f'Traffic Simulation - Step {step_counter}\nActive Cars: {active_cars}/{len(carros)}', fontsize=14)
        ax.set_xlabel('X', fontsize=12)
        ax.set_ylabel('Y', fontsize=12)
        
        if step_counter % 10 == 0:
            print(f"Step {step_counter}: {active_cars} cars still moving")
        
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        time.sleep(0.1)
    
    print(f"\nSimulation ended after {step_counter} steps!")
    print(f"All {len(carros)} cars reached their destinations!")
    
    plt.ioff()
    plt.show()