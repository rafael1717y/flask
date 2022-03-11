# Importando a variável app definida dentro pacote app
from flask import render_template
from app import app


# Decorator para associação do '/' e '/index' com a função
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rafael'}
    posts = [
        {
            'author':{'username': 'John'},
            'body': 'Um belo dia!', 
        },
        {
            'author': {'username':'Sissi'}, 
            'body': 'Nada aqui!'
        },        
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)