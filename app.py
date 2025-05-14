from flask import Flask, url_for

app = Flask(__name__, static_folder='img')

@app.route('/')
def home():
    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Página Web Profesional</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                color: #333;
                margin: 0;
                padding: 20px;
            }}
            header, footer {{
                background-color: #004080;
                color: white;
                text-align: center;
                padding: 10px 0;
            }}
            .content {{
                margin: 20px 0;
            }}
            img {{
                width: 20%;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>Bienvenido a mi página web profesional</h1>
        </header>

        <div class="content">
            <h2>Sobre mí</h2>
            <p>Soy estudiante de la carrera de Administración de Centros de Cómputo.</p>
            <p>Este proyecto fue desarrollado con <strong>Python</strong> y <strong>Flask</strong>.</p>
        </div>

        <div class="content">
            <h2>Conocimientos aplicados</h2>
            <p>Aplicación de conocimientos en:</p>
            <ul>
                <li>Gestión de infraestructura tecnológica</li>
                <li>Redes y soporte técnico</li>
                <li>Desarrollo web</li>
                <li>Centros de procesamiento de datos</li>
            </ul>
        </div>

        <div class="content">
            <h2>Imagen Representativa</h2>
            <img src="{url_for('static', filename='sistema-informatico-1-e1585504699254.jpg')}" alt="Imagen de ejemplo del proyecto">
        </div>

        <footer>
            <p>Desarrollado por [Gavilan Morales Gerson Paul] &copy; 2025</p>
        </footer>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
