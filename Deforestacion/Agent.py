#DEFORESTACION DE ARBOLES
"""
Importaciones de MESA
"""
import mesa

from mesa import Model, Agent


"""
Se realiza las celdas en las cuales se ubicaran los arboles
teniendo coordenadas X y Y
"""

class CeldasArboles(mesa.Agent):
    """
    Se definen las condiciones que podría tener un arbol
    Sano: El arbol no se encuentra incendiado
    En llamas: El arbol se encuentra en fuego actualmente
    Quemado: El arbol se encuentra incendiado
    """
    def __init__(self, pos, model):
        
        #Se crea un arbol nuevo
        
        super().__init__(pos, model)

        #Se definen atributos para la posicion y condicion
        self.pos = pos
        self.condicion = "Sano"

    def step(self):
        """
        Si el árbol está En llamas, se va esparcir 
        a los árboles cercanos.
        """
        if self.condicion == "En llamas":
            """
            Utilizamos get_neighbohrs para obtener los arboles cercanos al arbol
            que se encuentra en llamas, se le entrega como parametros la posicion(pos)
            y la funcion 'moore' que en este caso (=False) nos indica que los cercanos
            que tomará serán los que esten ubicados directamente adyacentes en las
            direcciones vertical y horizontal
            """
           
            for neighbor in self.model.grid.iter_neighbors(self.pos, True):
                if neighbor.condicion == "Sano":
                    neighbor.condicion = "En llamas"
            self.condicion = "Quemado"