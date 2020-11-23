class Cidade :
    def __init__(self,cidade, data, populacao, casos_confirmado, ultimas_mortes, estado, novos_confirmados, novas_mortes):
        self.cidade = cidade
        self.data = data
        self.populacao = int(populacao)
        self.casos_confirmado = int(casos_confirmado)
        self.ultimas_mortes = int(ultimas_mortes)
        self.estado = estado
        self.novos_confirmados = int(novos_confirmados)
        self.novas_mortes = int(novas_mortes.replace("\n",""))


    def __repr__(self):
        return f"{self.cidade} : {self.data}:{self.populacao} : {self.casos_confirmado} : {self.ultimas_mortes} : {self.estado} : {self.novos_confirmados}:{self.novas_mortes}" 


