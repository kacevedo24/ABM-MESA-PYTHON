"""
Se define la representacion del Modelo: la cuadricula, los tiempos,
el tamaño, la densidad de arboles y la colección de arboles

"""
import mesa
import Model
from Model import ModeloDeforestacion
import datetime

from mesa.visualization.modules import CanvasGrid, TextElement
from mesa.visualization.ModularVisualization import ModularServer

def get_arboles_sanos(Model):
    data = Model.datacollector.get_model_vars_dataframe()
    arboles_sanos_data = data["Sano"]
    ultimo_valor = arboles_sanos_data.iloc[-1]  # Obtener el último valor de los árboles sanos
    return f"ARBOLES SANOS: {ultimo_valor}"

def get_arboles_incendiados(Model):
    data = Model.datacollector.get_model_vars_dataframe()
    arboles_sanos_data = data["En llamas"]
    ultimo_valor = arboles_sanos_data.iloc[-1]  # Obtener el último valor de los árboles sanos
    return f"ARBOLES SANOS: {ultimo_valor}"

def get_arboles_quemados(Model):
    data = Model.datacollector.get_model_vars_dataframe()
    arboles_sanos_data = data["Quemado"]
    ultimo_valor = arboles_sanos_data.iloc[-1]  # Obtener el último valor de los árboles sanos
    return f"ARBOLES SANOS: {ultimo_valor}"

class TiempoTranscurridoElement(TextElement):
    def render(self, model):
        tiempo_actual = datetime.datetime.now()
        tiempo_transcurrido = tiempo_actual - model.tiempo_inicial
        segundos_transcurridos = tiempo_transcurrido.seconds
        return f"SEGUNDOS TRANSCURRIDOS: {segundos_transcurridos}"
    
tiempo_transcurrido_element = TiempoTranscurridoElement()

#Se inicia creando la cuadricula con los argumentos que toma el modelo
colores = {"Sano": "#00FF00", "En llamas": "#FF0000", "Quemado": "#000000"}

def forest_fire_portrayal(arbol):
    if arbol is None:
        return
    portrayal = {"Shape": "circle", "r" : 1, "Filled": "true", "Layer": 0}
    (x, y) = arbol.pos
    portrayal["x"] = x
    portrayal["y"] = y
    portrayal["Color"] = colores[arbol.condicion]
    return portrayal


canvas_element = mesa.visualization.CanvasGrid(
    forest_fire_portrayal, 100, 100, 400, 400
)


model_params = {
    "width": 100,
    "height": 100,
    "densidad": mesa.visualization.Slider("arbol densidad", 0.70, 0.01, 1.0, 0.01),
}
server = ModularServer(
    ModeloDeforestacion, [canvas_element, get_arboles_sanos, get_arboles_incendiados, get_arboles_quemados, 
                          tiempo_transcurrido_element], "MODELO DEFORESTACION DE ARBOLES", model_params
)
server.port=8522
server.launch()

