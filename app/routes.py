# Paso 1: importar las herramientas necesarias de Flask
from flask import render_template, request

# Paso 2: importar la app Flask desde __init__.py
from app import app

# Paso 3: definir la función principal que maneja la ruta "/"
@app.route('/', methods=['GET', 'POST'])
def index():
    # Paso 4: verificar si el método fue POST (formulario enviado)
    if request.method == 'POST':
        # Paso 5: obtener el valor del input llamado "device_ip"
        ip = request.form['device_ip']

        # Paso 6: por ahora solo imprimir la IP en consola
        print(f"IP recibida desde formulario: {ip}")

        # Paso 7: volver a cargar el formulario
        return render_template('index.html')

    # Si no se ha enviado formulario, simplemente mostrarlo
    return render_template('index.html')
