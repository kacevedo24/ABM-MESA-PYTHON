from flask import Flask, render_template
from mesa.visualization.ModularVisualization import VisualizationElement
from server import ModeloEmociones, cuadricula_emociones

app = Flask(__name__)

# Crear la visualización
canvas_element = VisualizationElement()
canvas_element.portrayal = cuadricula_emociones
model_element = VisualizationElement()
model_element.agent_portrayal = cuadricula_emociones

def layout():
    return render_template('index.html')

@app.route('/')
def index():
    return layout()

@app.route('/run')
def run_model():
    model = ModeloEmociones(width=20, height=20, density=0.5)
    canvas_element.setModel(model)
    model_element.setModel(model)
    return layout()

@app.route('/model')
def model():
    return model_element.html("500px", "500px")

@app.route('/canvas')
def canvas():
    return canvas_element.html("500px", "500px")

if __name__ == '__main__':
    app.run(debug=True)
