from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def ola():
    lista = ['Tetris', 'Super Mario', 'Pokemon Gold']
    return render_template('index.html', titulo='Jogos',
                           jogos=lista)


app.run(host="0.0.0.0", port="5000")


