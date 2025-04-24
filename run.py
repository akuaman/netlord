# Lo que queremos hacer:
# Iniciar la aplicación Flask si este archivo es ejecutado directamente

# Paso 1: importar la app desde el paquete app
# Fundamento: importación de módulos
from app import app

# Paso 2: ejecutar la app solo si se corre este archivo directamente
# Fundamento: control de ejecución con __name__
if __name__ == '__main__':
    app.run(debug=True)