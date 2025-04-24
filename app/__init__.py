# Lo que queremos hacer:
# Crear una instancia de la app Flask y conectar las rutas

# Paso 1: importar Flask
# Fundamento: importación de módulos
from flask import Flask

# Paso 2: crear la app
# Fundamento: definición de variables y pensamiento secuencial
app = Flask(__name__)

# Paso 3: importar las rutas (después de crear la app)
# Fundamento: estructura modular; se importa para registrar las rutas
from app import routes