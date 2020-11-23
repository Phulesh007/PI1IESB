import PySimpleGUI as sg
import funcao
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

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Qual algoritmo deseja utilizar?'),sg.Combo(['QuickSort', 'BubbleSort', 'SelectionSort', 'InsertionSort', 'MergeSort', 'Todos'] ,key='sort')],
            [sg.Text('O que deseja filtrar?'),sg.Combo(['Casos confirmados', 'Mortes', 'População'], key='filtro')],
            [sg.Button('Pesquisar')],
            [sg.Output()]
        ]
        # Janela
        self.janela = sg.Window("Filtro covid test").layout(layout)
        # Extrair os dados da tela
        self.button, self.values = self.janela.Read()
    
    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            sort = self.values['sort']
            filtro = self.values['filtro']
            
            if sort == 'QuickSort':
                aux = []
                aux2 = []
                if filtro == 'População':
                    funcao.retornalistapopulacao(bagulhosImportantes,aux)
                elif filtro == 'Casos confirmados':
                    funcao.retornalistacasos(bagulhosImportantes,aux)
                elif filtro == 'Mortes':
                    funcao.retornalistamortos(bagulhosImportantes,aux)       

                start = time.time()
                aux2 = Quicksort(aux)
                end = time.time()
                #print(aux2)
                print("tempo de ordenação com quick sort : {}".format(end - start))

            if sort == 'MergeSort':
                aux = []
                if filtro == 'População':
                    funcao.retornalistapopulacao(bagulhosImportantes,aux)
                elif filtro == 'Casos confirmados':
                    funcao.retornalistacasos(bagulhosImportantes,aux)
                elif filtro == 'Mortes':
                    funcao.retornalistamortos(bagulhosImportantes,aux)  

                start = time.time()
                Mergesort(aux)
                end = time.time()
                print("tempo de ordenação com merge sort : {}".format(end - start))

            if sort == 'InsertionSort':
                aux = []
                if filtro == 'População':
                    funcao.retornalistapopulacao(bagulhosImportantes,aux)
                elif filtro == 'Casos confirmados':
                    funcao.retornalistacasos(bagulhosImportantes,aux)
                elif filtro == 'Mortes':
                    funcao.retornalistamortos(bagulhosImportantes,aux)  
                start = time.time()
                Insertionsort(aux)

                end = time.time()
                print("tempo de ordenação com insertion sort : {}".format(end - start))

            if sort == 'SelectionSort':
                aux = []
                if filtro == 'População':
                    funcao.retornalistapopulacao(bagulhosImportantes,aux)
                elif filtro == 'Casos confirmados':
                    funcao.retornalistacasos(bagulhosImportantes,aux)
                elif filtro == 'Mortes':
                    funcao.retornalistamortos(bagulhosImportantes,aux) 
                    
                start = time.time()
                Selectionsort(aux)
                end = time.time()
                print("tempo de ordenação com selection sort : {}".format(end - start))

            if sort == 'InsertionSort':
                aux = []
                if filtro == 'População':
                    funcao.retornalistapopulacao(bagulhosImportantes,aux)
                elif filtro == 'Casos confirmados':
                    funcao.retornalistacasos(bagulhosImportantes,aux)
                elif filtro == 'Mortes':
                    funcao.retornalistamortos(bagulhosImportantes,aux)

                start = time.time()
                Bubblesort(aux)
                end = time.time()
                print("tempo de ordenação com bubble sort : {}".format(end - start))

            # if sort == 'Todos':
            #     start = time.time()
            #     QuickSort(lista)
            #     end = time.time()
            #     print("Tempo decorrido QuickSort: {}".format(end - start))

            #     start = time.time()
            #     Sort(lista)
            #     end = time.time()
            #     print("Tempo decorrido MergeSort: {}".format(end - start))

            #     start = time.time()
            #     InsertionSort(lista)
            #     end = time.time()
            #     print("Tempo decorrido InsertionSort: {}".format(end - start))

            #     start = time.time()
            #     SelectionSort(lista)
            #     end = time.time()
            #     print("Tempo decorrido SelectionSort: {}".format(end - start))

            #     start = time.time()
            #     BubbleSort(lista)
            #     end = time.time()
            #     print("Tempo decorrido BlubbleSort: {}".format(end - start))

tela = TelaPython()
tela.Iniciar()
