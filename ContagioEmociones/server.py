import mesa
from model import ModeloEmociones
from mesa.visualization.ModularVisualization import ModularServer, TextElement
from mesa.visualization.modules import CanvasGrid, TextElement
import datetime
from agent import Personas

COLORES = {
    "Felicidad": "yellow",
    "Tristeza": "blue",
    "Miedo": "purple",
    "Ira": "red"
}

class Emocion1CountElement(TextElement):
    def render(self, model):
        count = sum(1 for agent in model.schedule.agents if agent.get_estado() == "Felicidad")
        return f"Personas felices: {count}"
emocion1_count_element = Emocion1CountElement()

class Emocion2CountElement(TextElement):
    def render(self, model):
        count = sum(1 for agent in model.schedule.agents if agent.get_estado() =="Tristeza")
        return f"Personas tristes: {count}"
emocion2_count_element = Emocion2CountElement()

class Emocion3CountElement(TextElement):
    def render(self, model):
        count = sum(1 for agent in model.schedule.agents if agent.get_estado() == "Miedo")
        return f"Personas con miedo: {count}"
emocion3_count_element = Emocion3CountElement()

class Emocion4CountElement(TextElement):
    def render(self, model):
        count = sum(1 for agent in model.schedule.agents if agent.get_estado() == "Ira")
        return f"Personas con ira: {count}"
emocion4_count_element = Emocion4CountElement()

class EmocionComunElement(TextElement):
    def render(self, model):
        emociones_comunes = model.conteo_emociones.most_common()
        if emociones_comunes:
            emocion_mas_comun = emociones_comunes[0][0]
            return f"EMOCION CON MAS OCURRENCIAS: {emocion_mas_comun}"
        else:
            return "No hay emociones comunes"


emocion_comun_element = EmocionComunElement()

class TiempoTranscurridoElement(TextElement):
    def render(self, model):
        tiempo_actual = datetime.datetime.now()
        tiempo_transcurrido = tiempo_actual - model.tiempo_inicial
        segundos_transcurridos = tiempo_transcurrido.seconds
        return f"SEGUNDOS TRANSCURRIDOS: {segundos_transcurridos}"
    
tiempo_transcurrido_element = TiempoTranscurridoElement()

def cuadricula_emociones(celda):

    if celda is None:
        raise AssertionError
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}
    portrayal["Color"] = COLORES[celda.get_estado()]
    
    return portrayal

canvas_element = mesa.visualization.CanvasGrid(cuadricula_emociones, 20, 20, 400, 400)

server = mesa.visualization.ModularServer(
    ModeloEmociones,
    [canvas_element, tiempo_transcurrido_element, emocion_comun_element, emocion1_count_element, 
     emocion2_count_element, emocion3_count_element, emocion4_count_element],
    "MODELO CONTAGIO DE EMOCIONES",
    {"width": 20, "height": 20},
    
)
server.port= 8521
server.launch()

