from collections import Counter

import mesa


class Personas(mesa.Agent):
    """
    Contagio de emociones cada una representadas por un color
    """

    #Inicializar el agente
    def __init__(self, pos, model, estado):
        super().__init__(pos, model)

        #Se definen atributos para la posicion y condicion
        self.pos = pos
        self.estado = estado

    def get_estado(self):
        """Retorna el estado actual (emocion) de esta celda."""
        return self.estado

    def step(self):

        #se obtienen las personas vecinas 
        vecinos = self.model.grid.iter_neighbors(self.pos, True)

        #Se obtienen las emociones de los vecinos
        emociones_vecinos = [n.get_estado() for n in vecinos]

        """Se utiliza Counter para saber cuantas ocurrencias
        tiene cada emocion de la lista"""

        conteo_emociones = Counter(emociones_vecinos)
        
        #se ordena la lista de mayor a menor
        emociones_comunes = conteo_emociones.most_common()

        """Se selecciona  una emoción aleatoria de las
         emociones más comunes que tienen la misma frecuencia 
        que la emoción más común en la lista """
        emocion_elegida = self.random.choice([emocion[0] for emocion in emociones_comunes if emocion[1] == emociones_comunes[0][1]])

        # Se establece la emoción elegida como el siguiente estado del agente en el siguiente paso del modelo
        self.next_estado = emocion_elegida
        
    def advance(self):
        """
        Se cambia el estado de emocion del agente
        """
        self.estado = self.next_estado
