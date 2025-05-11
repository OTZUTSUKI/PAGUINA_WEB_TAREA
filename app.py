from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
        <h1>Bienvenido a mi página web profesional</h1>
        <p>Esta es una demostración de mi proyecto desarrollado con Python, como parte de mi formación en la carrera de Administración de Centros de Cómputo. 
        Aquí aplico conocimientos en gestión de infraestructura tecnológica, redes, soporte técnico y desarrollo web, fundamentales para el manejo eficiente 
        de centros de procesamiento de datos.</p>
    """

if __name__ == '__main__':
    app.run()

