# Importando a variável app definida dentro pacote app
from flask import flash, redirect, render_template, url_for
from app import app
from app.forms import LoginForm


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requestes for user {}, remeber_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)



