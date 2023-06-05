from agent import Personas
from collections import Counter
import mesa
from mesa.space import MultiGrid
import datetime


class ModeloEmociones(mesa.Model):
    """Este modelo presenta un fenómeno de emociones, donde cada agente se ve influenciado
    por las emociones predominantes entre sus agentes vecinos y cambia su estado emocional
    por la emoción con más ocurrencias."""

    #Emociones seleccionadas para el modelo
    EMOCIONES = ["Felicidad", "Tristeza", "Miedo", "Ira"]

    #Constructor
    def __init__(self, width=20, height=20):
        super().__init__()
        self.width = width
        self.height = height

        # Inicializar el atributo tiempo en 0
        self.tiempo_inicial = datetime.datetime.now()
                
        #Activacion aleatoria de los agentes
        self.schedule = mesa.time.SimultaneousActivation(self)

        #Creacion de un Multigrid que permita mas de 1 agente en la cuadricula
        self.grid = MultiGrid(width, height, torus=False)

        #Se inicia el modelo
        self.running = True

        """ Se recorren todas las celdas en la cuadrícula y 
            se crea un agente Personas en cada coordenada"""
    
        for x in range(self.width):
            for y in range(self.height):

                #Creacion de la celda, con los parametros posicion, modelo y estado
                persona = Personas((x, y), self, self.random.choice(ModeloEmociones.EMOCIONES))

                #Se coloca el agente en la coordenada
                self.grid.place_agent(persona, (x, y))

                #Se agrega a la activacion
                self.schedule.add(persona)



        # Se inicializa el atributo conteo_emociones como Counter
        self.conteo_emociones = Counter()  

    def step(self):
       
        # Paso del modelo
        self.schedule.step()

         # Actualizar el conteo de emociones en cada paso del modelo
        self.conteo_emociones = self.contar_emociones()

        # Verificar si una de las emociones está presente en todas las personas
        total_personas = len(self.schedule.agents)
        for emocion_count in self.conteo_emociones.values():
            if emocion_count == total_personas:

                #Detener el modelo
                self.running = False

    def contar_emociones(self):

        #Se llama al contador de emociones
        conteo = Counter()

        #Se cuentan las ocurrencias por emociones.
        for agent in self.schedule.agents:
            conteo[agent.get_estado()] += 1
        return conteo
