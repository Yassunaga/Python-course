from ..models.models import Jogo, Usuario

SQL_CRIA_JOGO = 'INSERT INTO jogo (nome, categoria, console) VALUES (%s, %s, %s)'
SQL_ATUALIZA_JOGO = 'UPDATE jogo SET nome=%s, categoria=%s, console=%s where id = %s'
SQL_BUSCA_JOGOS = ""

class JogoDao:
    def __init__(self, db):
        self.__db = db

    def salvar(self, jogo : Jogo):
        cursor = self.__db.connection.cursor()
        if jogo.id:
            cursor.execute(SQL_ATUALIZA_JOGO, (jogo.nome, jogo.categoria, jogo.console))
        else:
            cursor.execute(SQL_CRIA_JOGO, (jogo.nome, jogo.categoria, jogo.console))
            jogo.id = cursor.lastrowid
        self.__db.connection.commit()
        return jogo

    def listar(self):
        cursor = self.__db.connection.cursor()
        # cursor.execute(SQL)
