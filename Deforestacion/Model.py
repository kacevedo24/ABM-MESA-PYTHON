"""
Se define el Modelo: la cuadricula, los tiempos, el tamaño
la densidad de arboles y la colección de arboles
cuadricula
"""
import mesa
from mesa import Model
from Agent import CeldasArboles
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
from mesa.space import MultiGrid
import datetime
class ModeloDeforestacion(mesa.Model):
   """Este modelo representa la capacidad de propagacion en los arboles"""
   
   #Constructor
   def __init__(self, width=100, height=100, densidad=0.65):
      self.width = width
      self.height = height

      # Inicializar el momento exacto en el que se crea el modelo
      self.tiempo_inicial = datetime.datetime.now()

       #Activacion aleatoria para los agentes en cada paso de la simulación
      self.schedule = mesa.time.RandomActivation(self)

      """torus no permite que los agentes se salgan de la cuadricula
       si un agente se mueve más allá del borde de la cuadricula en una dirección, 
       aparecerá en el borde opuesto de la cuadricula en esa misma dirección.
       """
      self.grid = MultiGrid(width, height, torus = False)

       #Se cuentan los agentes de los tipos especificos "Sano", "En llamas", "Quemado"
      self.datacollector = mesa.DataCollector(
         {
           "Sano": lambda m: self.ConteoAux(m, "Sano"),
           "En llamas": lambda m: self.ConteoAux(m, "En llamas"),
           "Quemado": lambda m: self.ConteoAux(m, "Quemado"),
         }
      )

     #Se coloca un arbol en cada celda
      for (contents, x, y) in self.grid.coord_iter():
            if self.random.random() < densidad:
                
                # Creación de un arbol
                arbol_nuevo = CeldasArboles((x, y), self)

                # Configuración para incendiar la primer fila de arboles
                if x == 0:
                    arbol_nuevo.condicion = "En llamas"
                self.grid.place_agent(arbol_nuevo, (x, y))
                self.schedule.add(arbol_nuevo)

        #Se ejecuta la simulación
      self.running = True
      
      self.datacollector.collect(self)

   def step(self):
       
       #Aqui se define el paso que debe dar el modelo
       self.schedule.step()
       self.datacollector.collect(self)

       #Si no hay mas fuego, el modelo debe parar
       if self.ConteoAux(self, "En llamas") == 0:
          self.running = False

   @staticmethod
   def ConteoAux(model, condicion_arbol):
       """
       Método auxiliar para contar árboles en
       una condición dada en un modelo dado.
       """
       aux = 0
       for arbol in model.schedule.agents:
          if arbol.condicion == condicion_arbol:
             aux = aux + 1
       return aux
    