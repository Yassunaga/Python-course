class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.is_url_valida(url):
            self.url = url
        else:
            raise LookupError("Url inválida!!!")

    def __str__(self):
        return self.url

    @staticmethod
    def is_url_valida(url):
        if url:
            return True
        else:
            return False

    def extrai_argumentos(self):
        """O método find, recebe como segundo argumento, o ponto de partida da busca"""
        indice_inicial_moeda_origem = self.url.find("=") + 1
        indice_final_moeda_origem = self.url.find("&")

        indice_inicial_moeda_destino = self.url.find("=", 15) + 1
        indice_final_moeda_destino = self.url.find("&", self.url.find("&")+1)

        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]

        return moeda_origem, moeda_destino
