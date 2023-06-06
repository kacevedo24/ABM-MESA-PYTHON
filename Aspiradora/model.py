import mesa
import datetime
from agent import Aspiradora, Celdas
from mesa import Model
import random
from mesa.time import RandomActivation
from mesa.space import MultiGrid
class ModeloAspirar(Model):
    """El modelo aspiradora representa el comportamiento de una aspiradora donde su objetivo es limpiar
    todas las celdas que se encuentren sucias, para esto, enfrenta un nuevo agente Celda"""

    #Constructor
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height

        #Creacion de un Multigrid que permita mas de 1 agente en la cuadricula
        self.grid = MultiGrid(width, height, torus=False)

        #Activacion aleatoria de los agentes
        self.schedule = mesa.time.RandomActivation(self)

        # Inicializar el momento exacto en el que se crea el modelo
        self.tiempo_inicial = datetime.datetime.now()

        #Inicializar el contador de celdas limpias
        self.limpias = 0
       
        #Inicia el modelo
        self.running = True


        """ Se recorren todas las celdas en la cuadrícula y 
            se crea un agente Celda en cada coordenada"""

        for x in range(self.width):
            for y in range(self.height):

                #estado aleatorio para cada agente
                estado = self.random.choice(["Limpio", "Sucio"])

                #Se asigna un ID unico que esta dado por x y y
                unique_id = (x, y)

                #Creacion de la celda, con los parametros ID, posicion, estado y modelo
                celda_1 = Celdas(unique_id, (x, y), estado, self)

                #Se coloca el agente en la coordenada
                self.grid.place_agent(celda_1, (x, y))

                #Se agrega a la activacion
                self.schedule.add(celda_1)

        # Crear coordenadas aleatorias para asignarselas a la aspiradora
        x = self.random.randrange(self.grid.width)
        y= self.random.randrange(self.grid.height)

        #Crear el agente Aspiradora
        aspiradora = Aspiradora(0, self)

        #Ubicarlo en la cuadricula, en las coordenadas (x, y)
        self.grid.place_agent(aspiradora, (x, y))

        # Agregar la aspiradora a la lista de agentes activados en el modelo
        self.schedule.add(aspiradora) 

    def step(self):
        # Llamar al método "step()" del agente Aspiradora primero
        self.schedule.agents[1].step()

        # Luego, llamar al método "step()" de todos los otros agentes
        self.schedule.step()
              
        #Si no hay mas fuego, el modelo debe parar
        if self.ConteoAux(self, "Sucio") == 0:
           self.running = False
    @staticmethod
    def ConteoAux(model, estado_celda):
        """
        Método auxiliar para contar celdas en un estado
        dado en un modelo dado.
        """
        aux = 0
        for celda in model.schedule.agents:
            if isinstance(celda, Celdas) and celda.estado == estado_celda:
                aux = aux + 1
        return aux
