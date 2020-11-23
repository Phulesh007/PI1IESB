from Cidade import Cidade
from collections import defaultdict
from bubble import Bubblesort
from quick import Quicksort
from merge import Mergesort
from insertion import Insertionsort
from selection import Selectionsort
import funcao
import time


arquivo = open('dataSetFinal.txt',"r")

bagulhosImportantes = dict()

for linha in arquivo.readlines():
    if linha.startswith("Importados/Indefinidos"):
        continue
    aux = linha.split(';')
    #cidade = Cidade(aux[0],aux[1],aux[2],aux[4],aux[8],aux[9],aux[10],aux[11])
    cidade = Cidade(*aux)
    if cidade.estado not in bagulhosImportantes.keys():
        bagulhosImportantes[cidade.estado ] = defaultdict(list)
    bagulhosImportantes[cidade.estado][cidade.cidade].append(cidade)
    #print(cidade.populacao-)

arquivo.close()

#print(bagulhosImportantes)

# for item in bagulhosImportantes.keys():
#     print(item, " : ")
#     for item2 in bagulhosImportantes[item].keys():
#         print(item2, "\t : ")
#         for item3 in bagulhosImportantes[item][item2]:
#             print(item3)


#for item in bagulhosImportantes["19/08/2020"]["AC"]:
    
    #print(item.casos_confirmado)

# def nome(cidade):
#     return cidade.populacao

#bagulhosImportantes["19/08/2020"]["AC"].sort(key = nome, reverse = True )

#Bubblesort(bagulhosImportantes["19/08/2020"]["AC"])
#print(bagulhosImportantes["AC"]["Rio Branco"])

vetci = []
vetm = []
vetd = []

# for item in bagulhosImportantes["SP"]["São Paulo"]:
#     #print(item)
#     #print(item.data)
#     vetci.append(item.cidade)
#     vetm.append(item.ultimas_mortes) 

for item in bagulhosImportantes.keys():
    #print(item, " :************************************************************* ")
    for item2 in bagulhosImportantes[item].keys():
        #print(item2, "\t : ")
        #for item3 in bagulhosImportantes[item][item2]:
            
        vetci.append(item2)

    
    print(vetci)
#for i in range(len(vetci)):
    # print("cidade : {}Numero de mortes: {}".format(vetci[i],vetm[i]))
    

# for i in vetd:
#     print(i)

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

#print(pesquisa_binaria(vetci,"São Paulo"))



# def menu_funcs():
#         print("""
#                 Menu:
#                 (1) = Ordenar com QuickSort 
#                 (2) = Ordenar com MergeSort
#                 (3) = Ordenar com InsertionSort
#                 (4) = Ordenar com SelectionSort
#                 (5) = Ordenar com BlubbleSort
#                 (6) = Comparação entre os algoritmos
#                 (0) = Para SAIR
#         """)

#     # menu_funcs()
#         print("Qual a opção desejada? ")
#         opcao = int(input())

#         while(opcao != 0):
            
#             print("""
#                 Escolha uma opção:
#                 (1) = Ordenar população
#                 (2) = Ordenar casos confirmados
#                 (3) = Ordenar mortes
#                 (4) = Escolher um algoritmo
#                 (0) = Para SAIR
#         """)
#             opcaotipo = int(input())

#             if opcaotipo == 4:
#                 menu_funcs()

#             if opcaotipo == 0:
#                 print("Saindo do programa")
#                 quit()
            
#             if opcao == 1:
#                 aux = []
#                 aux2 = []
#                 if opcaotipo == 1:
#                     funcao.retornalistapopulacao(bagulhosImportantes,aux)
#                 elif opcaotipo == 2:
#                     funcao.retornalistacasos(bagulhosImportantes,aux)
#                 elif opcaotipo == 3:
#                     funcao.retornalistamortos(bagulhosImportantes,aux)       

#                 start = time.time()
#                 aux2 = Quicksort(aux)
#                 end = time.time()
#                 #print(aux2)
#                 print("tempo de ordenação com quick sort : {}".format(end - start))
#             elif opcao == 2:
#                 aux = []
#                 if opcaotipo == 1:
#                     funcao.retornalistapopulacao(bagulhosImportantes,aux)
#                 elif opcaotipo == 2:
#                     funcao.retornalistacasos(bagulhosImportantes,aux)
#                 elif opcaotipo == 3:
#                     funcao.retornalistamortos(bagulhosImportantes,aux)             

#                 start = time.time()
#                 Mergesort(aux)
#                 end = time.time()
#                 print("tempo de ordenação com merge sort : {}".format(end - start))
#             elif opcao == 3:
#                 aux = []
#                 if opcaotipo == 1:
#                     funcao.retornalistapopulacao(bagulhosImportantes,aux)
#                 elif opcaotipo == 2:
#                     funcao.retornalistacasos(bagulhosImportantes,aux)
#                 elif opcaotipo == 3:
#                     funcao.retornalistamortos(bagulhosImportantes,aux)      

#                 start = time.time()
#                 Insertionsort(aux)

#                 end = time.time()
#                 print("tempo de ordenação com insertion sort : {}".format(end - start))
#             elif opcao == 4:
#                 aux = []
#                 if opcaotipo == 1:
#                     funcao.retornalistapopulacao(bagulhosImportantes,aux)
#                 elif opcaotipo == 2:
#                     funcao.retornalistacasos(bagulhosImportantes,aux)
#                 elif opcaotipo == 3:
#                     funcao.retornalistamortos(bagulhosImportantes,aux)  

#                 start = time.time()
#                 Selectionsort(aux)
#                 end = time.time()
#                 print("tempo de ordenação com selection sort : {}".format(end - start))
#             elif opcao == 5:
#                 aux = []
#                 if opcaotipo == 1:
#                     funcao.retornalistapopulacao(bagulhosImportantes,aux)
#                 elif opcaotipo == 2:
#                     funcao.retornalistacasos(bagulhosImportantes,aux)
#                 elif opcaotipo == 3:
#                     funcao.retornalistamortos(bagulhosImportantes,aux)    

#                 start = time.time()
#                 Bubblesort(aux)

#                 end = time.time()
#                 print("tempo de ordenação com bubble sort : {}".format(end - start))
            
#             # elif opcao == 6:
#             #     ler_arquivo()
#             #     start = time.time()
#             #     QuickSort(lista)
#             #     end = time.time()
#             #     print("Tempo decorrido QuickSort: {}".format(end - start))

#             #     ler_arquivo()
#             #     start = time.time()
#             #     Sort(lista)
#             #     end = time.time()
#             #     print("Tempo decorrido MergeSort: {}".format(end - start))

#             #     ler_arquivo()
#             #     start = time.time()
#             #     InsertionSort(lista)
#             #     end = time.time()
#             #     print("Tempo decorrido InsertionSort: {}".format(end - start))

#             #     ler_arquivo()
#             #     start = time.time()
#             #     SelectionSort(lista)
#             #     end = time.time()
#             #     print("Tempo decorrido SelectionSort: {}".format(end - start))

#             #     ler_arquivo()
#             #     start = time.time()
#             #     BubbleSort(lista)
#             #     end = time.time()
#             #     print("Tempo decorrido BlubbleSort: {}".format(end - start))
            
#             elif opcao == 0 :
#                 print("Saindo do programa")
#                 quit()
#             else:
#                 print("Opção invalida")


# menu_funcs()