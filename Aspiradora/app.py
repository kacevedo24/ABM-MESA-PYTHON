from flask import Flask, render_template
from mesa.visualization.ModularVisualization import VisualizationElement
from server import ModeloAspirar, celdas_portrayal, get_agentes_limpios

app = Flask(__name__)

# Crear la visualización
canvas_element = VisualizationElement()
canvas_element.portrayal = celdas_portrayal
model_element = VisualizationElement()
model_element.agent_portrayal = celdas_portrayal

def layout():
    return render_template('index.html')

@app.route('/')
def index():
    return layout()

@app.route('/run')
def run_model():
    model = ModeloAspirar(width=20, height=20, density=0.5)
    canvas_element.setModel(model)
    model_element.setModel(model)
    return layout()

@app.route('/model')
def model():
    return model_element.html("500px", "500px")

@app.route('/canvas')
def canvas():
    return canvas_element.html("500px", "500px")

@app.route('/data')
def data():
    return get_agentes_limpios(model)

if __name__ == '__main__':
    app.run(debug=True)
