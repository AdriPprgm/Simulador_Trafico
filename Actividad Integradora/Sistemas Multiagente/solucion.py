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
        neighbors = diccionario_movimientos.movimientos_posibles[cell[0] + 1][cell[1] + 1]

        for i in neighbors:
            cell_pos = (i[0] - 1, i[1] - 1)
            if cell_pos not in visited:
                neighbor_cell = grid[cell_pos]
                has_car = any(isinstance(agent, Carro) for agent in neighbor_cell.agents)
                is_park = any(isinstance(agent, AgenteCalle) and agent.isEstacionamiento for agent in neighbor_cell.agents)
                if not has_car or is_park:
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
        self.estacionado = True

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
            self.remove()

# Modelo

class TrafficModel(mesa.Model):
    def __init__(self, n):
        super().__init__()
        self.num_cars = n
        self.grid = OrthogonalVonNeumannGrid((24, 24), torus = False, capacity = 100, random = self.random)
        self.estacionamientos_cells = []

        for x in range(width):
            for y in range(height):
                cell = self.grid[(x, y)]
                calle = AgenteCalle(self, cell)
                
                #Set Semaforos1
                if (x == 21 and (y == 4 or y == 5 or y == 10 or y == 11) or
                    x == 2 and (y == 4 or y == 5 or y == 8 or y == 9) or
                    x == 7 and (y == 22 or y == 23) or
                    x == 15 and (y == 22 or y == 23)):
                    semaforo1 = Semaforo1(self, cell)

                #Set Semaforos2
                if (y == 3 and (x == 0 or x == 1) or
                    y == 7 and (x == 0 or x == 1) or
                    y == 2 and (x == 10 or x == 11) or
                    y == 6 and (x == 22 or x == 23) or
                    y == 12 and (x == 22 or x == 23) or
                    y == 21 and (x == 8 or x == 9 or x == 16 or x == 17)):
                    semaforo2 = Semaforo2(self, cell)
        
                #Set Buildings
                if ((1 < x < 4) and (1 < y < 4) or
                    (1 < x < 4) and (5 < y < 8) or
                    (1 < x < 4) and (11 < y < 16) or
                    (1 < x < 8) and (17 < y < 22) or
                    (5 < x < 8) and (1 < y < 4) or
                    (5 < x < 8) and (5 < y < 8) or
                    (5 < x < 8) and (11 < y < 16) or
                    (11 < x < 22) and (1 < y < 4) or
                    (11 < x < 22) and (5 < y < 8) or
                    (11 < x < 16) and (11 < y < 15) or
                    (11 < x < 16) and (16 < y < 22) or
                    (17 < x < 22) and (11 < y < 22) or
                    (8 < x < 11) and (8 < y < 11)):
                    calle.isBuilding = True
                
                #Set Estacionamiento
                if ((x == 3 and y == 3) or  # Estacionamiento 13
                    (x == 7 and y == 6) or  # Estacionamiento 17
                    (x == 3 and y == 12) or  # Estacionamiento 12
                    (x == 6 and y == 15) or  # Estacionamiento 15
                    (x == 6 and y == 18) or  # Estacionamiento 16
                    (x == 4 and y == 21) or  # Estacionamiento 14
                    (x == 13 and y == 3) or  # Estacionamiento 2
                    (x == 14 and y == 6) or  # Estacionamiento 5
                    (x == 14 and y == 14) or  # Estacionamiento 3
                    (x == 12 and y == 18) or  # Estacionamiento 1
                    (x == 14 and y == 21) or  # Estacionamiento 4
                    (x == 20 and y == 2) or  # Estacionamiento 10
                    (x == 19 and y == 7) or  # Estacionamiento 8
                    (x == 19 and y == 12) or  # Estacionamiento 7
                    (x == 21 and y == 16) or  # Estacionamiento 11
                    (x == 18 and y == 19) or  # Estacionamiento 6
                    (x == 20 and y == 21)):  # Estacionamiento 9
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

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    
    print("Testing Carro agents with visualization...")
    
    width = 24
    height = 24
    model = TrafficModel(10)
    
    carros = [agent for agent in model.agents if isinstance(agent, Carro)]
    
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
        
        return grid_state
    
    colors = ['white', 'lightblue', 'blue', 'red', 'grey', 'green', 'black', 'cyan', 'yellow']
    cmap = ListedColormap(colors)
    
    step_counter = 0
    
    while any(not carro.estacionado for carro in carros):
        model.step()
        step_counter += 1
        
        grid_state = get_grid_state()
        
        ax.clear()

        sns.heatmap(grid_state, cmap=cmap, vmin=0, vmax=8,
                   square=True, linewidths=0.5, linecolor='gray',
                   cbar=False, ax=ax, annot=False)
        
        # Dibujar camellones
        ax.plot([10, 10], [2, 8], color='black', linewidth=3)
        ax.plot([10, 10], [12, 22], color='black', linewidth=3)
        ax.plot([2, 8], [10, 10], color='black', linewidth=3)
        ax.plot([12, 22], [10, 10], color='black', linewidth=3)
        
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