import csv
from Cidade import Cidade

with open('casos_full2.txt') as arquivo_csv:

    leitor = csv.reader(arquivo_csv, delimiter=';')

    entrada = input("digite a data: ")

    lista_data = []
    lista2 = []
    lista_mortes = []
    lista_cidades = []
    lista_estados = []
    lista_mortes2 = []
    lista_cidades2 = []

    c = 0
    for [cidade, data, populacao, populacao_2019, casos_confirmado, casos_confirmados_100k, ultima_data, ultima_taxa_mortes, ultimas_mortes, estado, novos_confirmados, novas_mortes] in leitor:

        # print ('{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(cidade, data, populacao, populacao_2019, casos_confirmado, casos_confirmados_100k, ultima_data, ultima_taxa_mortes, ultimas_mortes, estado, novos_confirmados, novas_mortes))
        # print(cidade)
            if(data == entrada):
                aux = data
                aux2 = int(ultimas_mortes)
                aux3 = cidade
                aux4 = estado
                lista_data.append(aux)
                lista_mortes.append(aux2)
                lista_cidades.append(aux3)
                lista_estados.append(aux4)
                


# print(lista)
# print("**")
# print(lista3)


    entrada2 = input("digite a sigla-UF do estado na : ")

for i in range(len(lista_estados)):
    count =0
    if(lista_estados[i] == entrada2):
        #print(i)
        lista_cidades2.append(lista_cidades[i])
        lista_mortes2.append(lista_mortes[i])
        
        #print("cidade : {}, Data: {}, Numero de mortes: {}, Estado {}: ".format(lista_cidades[i],lista_data[i],lista_mortes[i],lista_estados[i]))
        
for i in range(len(lista_mortes2)):
    print("cidade : {}Numero de mortes: {}".format(lista_cidades2[i],lista_mortes2[i]))
    

def qsort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        
        return qsort(less)+equal+qsort(greater)  
    
    else:  
        return array

def pesquisa_binaria(A, item):
    """Implementa pesquisa binária iterativamente."""
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] == item:
            return meio
        elif A[meio] > item:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1
    return -1


#lista2 = qsort(lista_mortes)

    
# print(lista2)
# print("**")

# print(pesquisa_binaria(lista2,0))






teste = {
        'SP' : {
             XS   'Cidades': [dados]
                } 
        
        
        }


teste["19/08/2020"]['SP']





