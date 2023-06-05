import mesa
from mesa import Agent, Model
from mesa.model import Model

class Aspiradora(Agent):
    #Inicializar el agente
    def __init__(self, pos, model):
        super().__init__(pos, model)

        #Se define el atributo posicion
        self.pos= pos
        
    def step(self):
        #print(f"Tiempo actual: {self.model.tiempo}")
        print(f"Celdas limpiadas: {self.model.limpias}")

        x, y = self.pos
        celda_actual = self.model.grid.get_cell_list_contents([self.pos])[0]
        print("paso")

        #Verifica si la celda en posicion actual esta sucia
        if celda_actual.estado == "Sucio":
            print(f"la celda {celda_actual.pos} necesita limpiarse")

            #Limpieza de celda
            celda_actual.estado = "Limpio"
            print(f"LIMPIEZA EXITOSA!!!")

            #Incremento de celdas limpias
            self.model.limpias += 1    
        else:
            pass

        #Se mueve
        self.move()
            
    def move(self):
        #Se identifica las celdas vecinas a la posicion actual.
        neighborhood = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)

        #Selecciona aleatoriamente una celda entre la lista de celdas obtenida
        new_pos = self.random.choice(neighborhood)

        #cambia la posicion actual por la posicion seleccionada
        self.model.grid.move_agent(self, new_pos)


class Celdas(Agent):
    #Se inicializa el agente Celda
    def __init__(self, unique_id, pos, estado, model):
        super().__init__(unique_id, model)

        #Se definen los atributos para la posicion y el estado
        self.pos= pos
        self.estado = estado
