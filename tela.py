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
import psutil

arquivo = open('dataSetFinal.txt',"r")

bagulhosImportantes = dict()

for linha in arquivo.readlines():
    if linha.startswith("Importados/Indefinidos"):
        continue
    aux = linha.split(';')
    cidade = Cidade(*aux)
    if cidade.estado not in bagulhosImportantes.keys():
        bagulhosImportantes[cidade.estado ] = defaultdict(list)
    bagulhosImportantes[cidade.estado][cidade.cidade].append(cidade)


arquivo.close()




class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Qual algoritmo deseja utilizar?'),sg.Combo(['QuickSort', 'BubbleSort', 'SelectionSort', 'InsertionSort', 'MergeSort', 'Todos'] ,key='sort')],
            [sg.Text('O que deseja filtrar?'),sg.Combo(['Casos confirmados', 'Mortes', 'População'], key='filtro')],
            [sg.Button('Pesquisar')],
            [sg.Output(size=(100,25))]
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
            funcoesFiltro = {'População':funcao.retornalistapopulacao,
                    'Mortes':funcao.retornalistamortos,
                    'Casos confirmados':funcao.retornalistacasos}

            aux = []
            aux2 = []
            
            if sort == 'QuickSort':
                funcoesFiltro[filtro](bagulhosImportantes,aux) 

                start = time.time()
                aux2 = Quicksort(aux)
                end = time.time()

                print("tempo de ordenação com quick sort : {}".format(end - start))
                aux.clear()

            if sort == 'MergeSort':
                funcoesFiltro[filtro](bagulhosImportantes,aux) 

                start = time.time()
                Mergesort(aux)
                end = time.time()

                print("tempo de ordenação com merge sort : {}".format(end - start))
                aux.clear()

            if sort == 'InsertionSort':
                funcoesFiltro[filtro](bagulhosImportantes,aux)  
                start = time.time()
                Insertionsort(aux)

                start = time.time()
                Insertionsort(aux)
                end = time.time()

                print("tempo de ordenação com insertion sort : {}".format(end - start))
                aux.clear()

            if sort == 'SelectionSort':
                funcoesFiltro[filtro](bagulhosImportantes,aux) 
                    
                start = time.time()
                Selectionsort(aux)
                end = time.time()

                print("tempo de ordenação com selection sort : {}".format(end - start))
                aux.clear()

            if sort == 'InsertionSort':
                funcoesFiltro[filtro](bagulhosImportantes,aux) 

                start = time.time()
                Bubblesort(aux)
                end = time.time()

                print("tempo de ordenação com bubble sort : {}".format(end - start))
                aux.clear()

            if sort == 'Todos':
                funcoesFiltro[filtro](bagulhosImportantes,aux) 

                start = time.time()
                aux2 = Quicksort(aux)
                end = time.time()

                print("tempo de ordenação com quick sort : {}".format(end - start))
                aux.clear()

                #***************************************
                
                funcoesFiltro[filtro](bagulhosImportantes,aux)  

                start = time.time()
                Mergesort(aux)
                end = time.time()

                print("tempo de ordenação com merge sort : {}".format(end - start))
                aux.clear()

                #*************************************
                funcoesFiltro[filtro](bagulhosImportantes,aux)    

                
                start = time.time()
                Insertionsort(aux)
                end = time.time()
                print("tempo de ordenação com insertion sort : {}".format(end - start))
                aux.clear()
                #***********************************
                funcoesFiltro[filtro](bagulhosImportantes,aux)   

                start = time.time()
                Selectionsort(aux)
                end = time.time()

                print("tempo de ordenação com selection sort : {}".format(end - start))
                aux.clear()
                #************************************
                funcoesFiltro[filtro](bagulhosImportantes,aux) 

                start = time.time()
                Bubblesort(aux)
                end = time.time()

                print("tempo de ordenação com bubble sort : {}".format(end - start))
                aux.clear()

tela = TelaPython()
tela.Iniciar()
