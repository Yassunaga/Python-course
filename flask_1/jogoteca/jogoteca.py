from flask import Flask, render_template, request, redirect, session, flash
from loguru import logger

app = Flask(__name__)
app.secret_key = "ULTRA SECRETO"


class Jogo:

    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

    def __str__(self):
        return f"{self.nome}, {self.console}, {self.categoria}"


jogo1 = Jogo("Mario", "Plataforma", "SNES")
jogo2 = Jogo("Mortal Kombat", "Luta", "SNES")
jogo3 = Jogo("Rayman", "Plataforma", "Xbox")

lista = [jogo1, jogo2, jogo3]


@app.route("/")
def index():
    logger.info("ABRINDO PÁGINA INICIAL")
    return render_template('index.html', jogos=lista, titulo="Jogoteca")


@app.route('/novo')
def novo():
    logger.info("CADASTRANDO NOVO JOGO")
    return render_template('novo.html')


@app.route("/criar", methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    novo_jogo = Jogo(nome, categoria, console)
    lista.append(novo_jogo)
    logger.info("CADASTRANDO NOVO JOGO")
    logger.info(f"{nome}")

    return redirect("/")


@app.route("/autenticar", methods=['POST'])
def autenticar():
    usuario = request.form['usuario']
    senha = request.form['senha']
    session['usuario_logado'] = usuario

    if senha == 'mestra':
        flash(f"Usuário {usuario} logado com sucesso!")
        return redirect("/")
    else:
        flash("Usuário ou senha incorretos!")
        return redirect("/login")


@app.route('/login')
def login():
    return render_template("login.html")


app.run(host="0.0.0.0", port=5000, debug=True)
logger.info("INICIANDO APLICAÇÃO")
