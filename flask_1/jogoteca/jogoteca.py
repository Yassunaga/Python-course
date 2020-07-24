from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_mysqldb import MySQL

from dao.dao import JogoDao, UsuarioDao
from models.models import Jogo

app = Flask(__name__)
app.secret_key = 'alura'

app.config['MYSQL_HOST'] = '0.0.0.0'
app.config['MYSQL_USER'] = 'yassunaga'
app.config['MYSQL_PASSWORD'] = '92875087'
app.config['MYSQL_DB'] = 'jogoteca'
app.config['MYSQL_PORT'] = 3306

db = MySQL(app)
jogo_dao = JogoDao(db)
usuario_dao = UsuarioDao(db)


@app.route('/')
def index():
    lista = jogo_dao.listar()
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST', ])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    jogo_dao.salvar(jogo)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = usuario_dao.buscar_por_id(request.form['usuario'])
    if usuario:
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado'] is None:
        return redirect(url_for('login', proxima=url_for('editar')))
    jogo_buscado = jogo_dao.busca_por_id(id)
    return render_template('editar.html', titulo='Editando jogo', jogo=jogo_buscado)


@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):

    jogo_buscado = jogo_dao.busca_por_id(id)
    jogo_buscado.nome = request.form['nome']
    print(request.form['nome'])

    jogo_buscado.categoria = request.form['categoria']
    print(request.form['categoria'])

    jogo_buscado.console = request.form['console']
    print(request.form['console'])

    print(jogo_buscado.nome)
    print(jogo_buscado.categoria)
    print(jogo_buscado.console)
    print(jogo_buscado.id)
    jogo_dao.salvar(jogo_buscado)

    return redirect(url_for('index'))


app.run(debug=True)
