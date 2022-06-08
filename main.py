# Python v3.10.4
# Flask v2.1.2
# Bootstrap v5.2.x
from flask import Flask, render_template, url_for, request
from forms import FormLogin, FormCriarConta


app = Flask(__name__)
app.config['SECRET_KEY'] = '588c8bc829117bc81c7e01fd0472eddc'

lista_usuarios = ['Lira', 'João', 'Alan', 'Alessandra', 'Amanda'] #página contato


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    
    if form_login.validate_on_submit() and 
    
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)