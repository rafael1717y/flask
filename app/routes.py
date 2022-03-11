# Importando a variável app definida dentro pacote app
from app import app


# Decorator para associação do '/' e '/index' com a função
@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'
