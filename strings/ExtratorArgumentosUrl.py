class ExtratorArgumentosUrl:
    URL_BYTE_BANK = "https://bytebank.com"

    def __init__(self, url: str):
        if self.is_url_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("Url inválida!!!")

    def __str__(self):
        valor = self.extrai_valor()
        moeda_origem, moeda_destino = self.extrai_argumentos()
        return "Valor: {} \nMoeda origem: {}\nMoeda destino: {}\n".format(valor, moeda_origem, moeda_destino)

    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        if isinstance(other, ExtratorArgumentosUrl):
            return self.url == other.url
        return False

    def is_url_valida(self, url):
        if url and url.startswith(self.URL_BYTE_BANK):
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
        fim_moeda_destino = self.url.find("&valor")

        moeda_destino = self.url[inicio_moeda_destino:fim_moeda_destino]
        return moeda_origem, moeda_destino

    def encontra_indice_inicial(self, moeda_buscada):
        return self.url.find(moeda_buscada) + len(moeda_buscada)

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino", "real", 1)

    def extrai_valor(self):
        busca_valor = "valor="
        indice_inicial_valor = self.encontra_indice_inicial(busca_valor)

        return self.url[indice_inicial_valor:]
