from pickle import APPEND
from flask_login import login_user, login_required, logout_user
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from .models import Catalogo
from . import db

auth = Blueprint('auth', __name__)



@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('emali')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=email).first()
    
    # verifica se o usuário realmente existe
    # pegue a senha fornecida pelo usuário, faça o hash e compare-a com a senha com hash no banco de dados
    if not User or not check_password_hash(User.password, password):
        flash('Login incorreto, verifique e tente novamente.')
        return redirect(url_for('auth.login')) # se o usuário não existir ou a senha estiver errada, recarregue a página
    # se a verificação acima for aprovada, sabemos que o usuário tem as credenciais corretas
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))
    


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    # código para validar e adicionar usuário ao banco de dados
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    
    User = User.query.filter_by(email=email).first()
    if User: # se um usuário for encontrado, queremos redirecionar de volta para a página de inscrição para que o usuário possa tentar novamente
        flash('O endereço de e-mail já existe. Ir para a página de login')
        return redirect(url_for('auth.signup'))
    
     # crie um novo usuário com os dados do formulário. Faça o hash da senha para que a versão em texto simples não seja salva.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
   
    # adicionar o novo usuário ao banco de dados
    db.session.add(new_user)
    db.session.commit()
       
    return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))



@auth.route('/catalogo', methods=["GET", "POST"])
def lista_catalogo():              
    return render_template('catalogo.html', Catalogo=Catalogo.query.all())



@auth.route('/cria_catalogo', methods=["GET", "POST"])
def cria_catalogo():
    #envio de informaçoes para o banco
    if request.method == 'POST':
        
        nome = request.form.get('nome')
        complexidade = request.form.get('complexidade')
        escopo = request.form.get('escopo')
        tempo = request.form.get('tempo')
        entregaveis = request.form.get('entregaveis')
        perfil = request.form.get('perfil')
        atividades = request.form.get('atividades')
            
        new_catalogo = Catalogo(
            nome=nome,
            complexidade=complexidade,
            escopo=escopo,
            tempo=tempo,
            entregaveis=entregaveis,
            perfil=perfil,
            atividades=atividades
            )
        
        db.session.add(new_catalogo)
        db.session.commit()                      
    return render_template('novo_catalogo.html')

