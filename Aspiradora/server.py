from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, TextElement
from agent import Aspiradora, Celdas
from model import ModeloAspirar
import datetime

def get_agentes_limpiados(model):
    # contador de celdas limpias
    return f"CELDAS QUE HAN SIDO LIMPIADAS: {model.limpias}"

class TiempoTranscurridoElement(TextElement):
    def render(self, model):
        tiempo_actual = datetime.datetime.now()
        tiempo_transcurrido = tiempo_actual - model.tiempo_inicial
        segundos_transcurridos = tiempo_transcurrido.seconds
        return f"SEGUNDOS TRANSCURRIDOS: {segundos_transcurridos}"
    
tiempo_transcurrido_element = TiempoTranscurridoElement()

def celdas_portrayal(celda):
    if celda is None:
        return None

    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0}

    if isinstance(celda, Celdas):
        if celda.estado == "Limpio":
            portrayal["Color"] = "white"
        else:
            portrayal["Color"] = "purple"
        portrayal["Layer"] = 0
    elif isinstance(celda, Aspiradora):
        portrayal = {"Shape": "circle", "r": 0.5, "Color": "pink", "Filled": "true","stroke_color": "red" , "Layer" : 1}
    return portrayal


grid = CanvasGrid(celdas_portrayal, 20, 20, 400, 400)

server = ModularServer(
    ModeloAspirar,
    [grid, get_agentes_limpiados, tiempo_transcurrido_element],
    "MODELO ASPIRADORA",
    {"width": 20, "height": 20},
)
server.port = 8520
server.launch()
