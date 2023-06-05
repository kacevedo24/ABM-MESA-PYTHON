import mesa
from agent import Religiosos
import datetime
from mesa.space import MultiGrid

class Religion_modelo(mesa.Model):
    """Este modelo representa el comportamiento de dos grupos de agentes que se dividen por religión, 
    según su tendencia (Cantidad de agentes del mismo tipo que deben conformar el grupo para que un agente se sienta satisfecho)"""

    # Constructor
    def __init__(self, width=20, height=20, density=0.5, proporcion=0.5, tendencia=4):
        self.width = width
        self.height = height
        # La densidad de los agentes
        self.density = density  

        # La proporción inicial para los grupos de agentes
        self.proporcion = proporcion  

        # El número mínimo de vecinos del mismo tipo para alcanzar satisfacción
        self.tendencia = tendencia  

        # Creación de un MultiGrid para la cuadrícula
        self.grid = MultiGrid(width, height, torus=False) 

        # Activación aleatoria de los agentes 
        self.schedule = mesa.time.RandomActivation(self) 

        # Inicializar el momento exacto en el que se crea el modelo 
        self.tiempo_inicial = datetime.datetime.now()  

        # Inicia el modelo
        self.running = True  

        # Inicializar el contador de agentes satisfechos
        self.agentes_satisfechos = 0  

        # Recorren todas las celdas en la cuadrícula y se crea un agente Religiosos en cada coordenada
        for x in range(self.width):
            for y in range(self.height):

                # Se asignan las condiciones de colectividad a partir de factores estocásticos
                if self.random.random() < self.density:
                    if self.random.random() < self.proporcion:
                        agente_tipo = 1
                    else:
                        agente_tipo = 0

                    # Creación del agente Religiosos con los parámetros posición, modelo y condición de grupo
                    agent = Religiosos((x, y), self, agente_tipo)

                    # Se coloca el agente en la coordenada
                    self.grid.place_agent(agent, (x, y))

                    # Se agrega a la activación
                    self.schedule.add(agent)

    def step(self):
        # Se activan los agentes
        self.schedule.step()

        # Actualizar el contador de agentes satisfechos en el modelo
        self.agentes_satisfechos = sum(agent.satisfecho for agent in self.schedule.agents)

        # Si la cantidad de agentes con satisfacción es la misma que el recuento de agentes
        if self.agentes_satisfechos == self.schedule.get_agent_count():
            
            # Se detiene el modelo
            self.running = False
