import mesa


class Religiosos(mesa.Agent):

    def __init__(self, pos, model, agente_tipo):
        """ Se crea un nuevo agente con tendencia de religion
           x, y: posicion inicial de los agentes
           agente_tipo: division de grupo: agente_tipo = 1 o agente_tipo = 0
        """
        #Atributos de los agentes para posicion, tipo de agente y si esta satisfecho
        super().__init__(pos, model)
        self.pos = pos
        self.tipo = agente_tipo
        self.satisfecho = False  

    def step(self):
        """ Se obtienen los agentes vecinos con la funcion iter_neighbors
            Si, el vecino tiene el mismo tipo de grupo se suma la variable similar
        """
        similar = 0
        for vecino in self.model.grid.iter_neighbors(self.pos, True):
            if vecino.tipo == self.tipo:
                similar += 1

        # Si la cantidad de similares es menor a la tendencia dada, mover:
        if similar < self.model.tendencia:
            # Se mueve a una celda vacía
            self.model.grid.move_to_empty(self)
            self.satisfecho = False
        else:
            """Si la cantidad de similares es igual o mayor
              a la tendencia, entonces el agente está "feliz" y
                se incrementa la variable agentes_satisfechos del modelo en uno."""
            self.satisfecho = True
            self.model.agentes_satisfechos += 1