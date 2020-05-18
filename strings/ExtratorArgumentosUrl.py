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
        busca_moeda_origem = "moedaorigem="
        busca_moeda_destino = "moedadestino="

        inicio_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
        fim_moeda_origem = self.url.find("&")
        moeda_origem = self.url[inicio_moeda_origem:fim_moeda_origem]

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            inicio_moeda_origem = self.encontra_indice_inicial(busca_moeda_origem)
            fim_moeda_origem = self.url.find("&")
            moeda_origem = self.url[inicio_moeda_origem:fim_moeda_origem]

        inicio_moeda_destino = self.encontra_indice_inicial(busca_moeda_destino)
        moeda_destino = self.url[inicio_moeda_destino:]
        return moeda_origem, moeda_destino

    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)
