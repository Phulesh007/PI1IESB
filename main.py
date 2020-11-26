from Cidade import Cidade
from collections import defaultdict
from bubble import Bubblesort
from quick import Quicksort
from merge import Mergesort
from insertion import Insertionsort
from selection import Selectionsort
import funcao
import time


arquivo = open('dataSetFinal2.txt',"r")
arquivo2 = open('dataSetFinal2orga.txt',encoding="utf8")

dataset = dict()

for linha in arquivo.readlines():
    if linha.startswith("Importados/Indefinidos"):
        continue
    aux = linha.split(';')
    cidade = Cidade(*aux)
    if cidade.estado not in dataset.keys():
        dataset[cidade.estado ] = defaultdict(list)
    dataset[cidade.estado][cidade.data].append(cidade)

nomes = []


for linha in arquivo2.readlines():
    
    palavras = linha.split(';')
    nomes.append(palavras[0])

arquivo.close()
arquivo2.close()

funcoesFiltro = {1:funcao.retornalistapopulacao,
                    2:funcao.retornalistacasos,
                    3:funcao.retornalistamortos}

def menu_funcs():
    print("""
            Menu:
            (1) = Ordenar com QuickSort 
            (2) = Ordenar com MergeSort
            (3) = Ordenar com InsertionSort
            (4) = Ordenar com SelectionSort
            (5) = Ordenar com BlubbleSort
            (6) = Todos os algorítmos
            (7) = Buscar uma cidade  
            (0) = Para SAIR
    """)
    aux = []
    aux2 = []

    print("Qual a opção desejada? ")
    opcao = int(input())

    while(opcao != 0):

        if opcao == 7:
            # a = input("Digite o estado da cidade que está buscando: ")
            # b = input("Digite a data: ")
            c = input("Digite a cidade que busca: ")

            # lista=[]

            # for item in dataset[a][b]:
            #     lista.append(item.cidade)            

            start = time.time()
            print(start)
            ret = funcao.pesquisa_binaria(nomes,c)
            end = time.time()
            print(end)

            print("O tempo para buscar a cidade {} foi de: {}".format(c,(end - start)))
            print(ret)
            menu_funcs()
        
        print("""
            Escolha uma opção:
            (1) = Ordenar população
            (2) = Ordenar casos confirmados
            (3) = Ordenar mortes
            (4) = Escolher um algoritmo
            (0) = Para SAIR
            """)
        opcaotipo = int(input())

        if opcaotipo == 4:
            menu_funcs()
        
        if (opcao == 0) or (opcaotipo == 0) :
            print("Saindo do programa")
            quit()
        elif opcao == 1:
            funcoesFiltro[opcaotipo](dataset,aux)     

            start = time.time()
            aux2 = Quicksort(aux)
            end = time.time()

            print("tempo de ordenação com quick sort : {}".format(end - start))
            aux.clear()

        elif opcao == 2:
            funcoesFiltro[opcaotipo](dataset,aux)                 

            start = time.time()
            Mergesort(aux)
            end = time.time()

            print("tempo de ordenação com merge sort : {}".format(end - start))
            aux.clear()

        elif opcao == 3:
            funcoesFiltro[opcaotipo](dataset,aux)       

            start = time.time()
            Insertionsort(aux)
            end = time.time()

            print("tempo de ordenação com insertion sort : {}".format(end - start))
            aux.clear()

        elif opcao == 4:
            funcoesFiltro[opcaotipo](dataset,aux)     

            start = time.time()
            Selectionsort(aux)
            end = time.time()

            print("tempo de ordenação com selection sort : {}".format(end - start))
            aux.clear()

        elif opcao == 5:
            funcoesFiltro[opcaotipo](dataset,aux)  

            start = time.time()
            Bubblesort(aux)
            end = time.time()

            print("tempo de ordenação com bubble sort : {}".format(end - start))
            aux.clear()     

        elif opcao == 6:
            funcoesFiltro[opcaotipo](dataset,aux) 

            start = time.time()
            aux2 = Quicksort(aux)
            end = time.time()

            print("tempo de ordenação com quick sort : {}".format(end - start))
            aux.clear()

            #***************************************
            
            funcoesFiltro[opcaotipo](dataset,aux)  

            start = time.time()
            Mergesort(aux)
            end = time.time()

            print("tempo de ordenação com merge sort : {}".format(end - start))
            aux.clear()

            #*************************************
            funcoesFiltro[opcaotipo](dataset,aux)    

            start = time.time()
            Insertionsort(aux)
            end = time.time()

            print("tempo de ordenação com insertion sort : {}".format(end - start))
            aux.clear()

            #***********************************
            funcoesFiltro[opcaotipo](dataset,aux)   

            start = time.time()
            Selectionsort(aux)
            end = time.time()

            print("tempo de ordenação com selection sort : {}".format(end - start))
            aux.clear()

            #************************************
            funcoesFiltro[opcaotipo](dataset,aux) 

            start = time.time()
            Bubblesort(aux)
            end = time.time()

            print("tempo de ordenação com bubble sort : {}".format(end - start))
            aux.clear()

        else:
            print("Opção invalida")

menu_funcs()

