import mesa
from model import Religion_modelo
import datetime
from mesa.visualization.modules import ChartModule, TextElement

def get_agentes_religiosos(model):
    return f"AGENTES SATISFECHOS: {model.agentes_satisfechos}"

class TiempoTranscurridoElement(TextElement):
    def render(self, model):
        tiempo_actual = datetime.datetime.now()
        tiempo_transcurrido = tiempo_actual - model.tiempo_inicial
        segundos_transcurridos = tiempo_transcurrido.seconds
        return f"SEGUNDOS TRANSCURRIDOS: {segundos_transcurridos}"

tiempo_transcurrido_element = TiempoTranscurridoElement()

def grid_Religiosos(agent):
    if agent is None:
        return
    portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Layer": 0}
    if agent.tipo == 0:
        portrayal["Color"] = ["pink"]
        portrayal["stroke_color"] = "#000000"
    else:
        portrayal["Color"] = ["#0000FF"]
        portrayal["stroke_color"] = "#000000"
    return portrayal


canvas_element = mesa.visualization.CanvasGrid(grid_Religiosos, 20, 20, 400, 400)


model_params = {
    "height": 20,
    "width": 20,
    "density": mesa.visualization.Slider("Densidad de agentes", 0.8, 0.1, 1.0, 0.1),
    "proporcion": mesa.visualization.Slider("Proporción", 0.2, 0.00, 1.0, 0.05),
    "tendencia": mesa.visualization.Slider("Tendencia", 3, 0, 8, 1),
}

server = mesa.visualization.ModularServer(
    Religion_modelo,
    [canvas_element, get_agentes_religiosos, tiempo_transcurrido_element],
    "MODELO GRUPOS RELIGIOSOS",
    model_params,
)

server.port = 8523
server.launch()