from flask import Flask, render_template, request

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo("Super Mario", "Plataforma", "SNES")
jogo2 = Jogo("Pokemon Gold", "RPG", "GameBoy")
jogo3 = Jogo("Mortal Kombat", "Luta", "SNES")

lista = [jogo1, jogo2, jogo3]


@app.route("/")
def index():
    return render_template('index.html', titulo='Jogos',
                           jogos=lista)


@app.route("/novo")
def novo():
    return render_template("novo.html", titulo="Novo Jogo")


@app.route("/criar", methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template("index.html", titulo='Jogos', jogos=lista)


app.run(host="0.0.0.0",
        port="5000",
        debug=True)