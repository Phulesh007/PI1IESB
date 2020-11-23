import csv
import time
import PySimpleGUI as sg

sort = ''
filtro = ''
list2 = []
lista2 = []
lista = []

with open('Arquivo/casos_full2.csv') as arquivo_csv:

        leitor = csv.reader(arquivo_csv, delimiter=';')
        
        for [cidade, data, populacao, populacao_2019, casos_confirmado, casos_confirmados_100k, ultima_data, ultima_taxa_mortes, ultimas_mortes, estado, novos_confirmados, novas_mortes] in leitor:

            # print ('{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(cidade, data, populacao, populacao_2019, casos_confirmado, casos_confirmados_100k, ultima_data, ultima_taxa_mortes, ultimas_mortes, estado, novos_confirmados, novas_mortes))
            # print(cidade)
            aux = int(ultimas_mortes)
            lista.append(aux)

def QuickSort(array):
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

        return QuickSort(less)+equal+QuickSort(greater)

    else:
        return array

def BubbleSort(vetor):

        for final in range(len(vetor), 0, -1):
            flag = False

            for i in range(0, final - 1):
                if vetor[i] > vetor[i + 1]:
                    vetor[i + 1], vetor[i] = vetor[i], vetor[i + 1]
                    flag = True

            if not flag:
                break

def Sort(vetor):
    aux = vetor[:]
    MergeSort(vetor, aux, 0, len(vetor) - 1)


def MergeSort(vetor, aux, start, end):
    if start >= end:
        return

    meio = (start + end) // 2

    MergeSort(vetor, aux, start, meio)
    MergeSort(vetor, aux, meio + 1, end)

    ordena(vetor, aux, start, end)


def ordena(vetor, aux, start, end):
    i = start
    ifim = (start + end) // 2

    j = ifim + 1
    jfim = end

    for p in range(start, end + 1):
        if i > ifim:
            aux[p] = vetor[j]
            j += 1

        elif j > jfim:
            aux[p] = vetor[i]
            i += 1

        elif vetor[i] < vetor[j]:
            aux[p] = vetor[i]
            i += 1

        else:
            aux[p] = vetor[j]
            j += 1

    for k in range(start, end + 1):
        vetor[k] = aux[k]

def SelectionSort(vetor):
    for i in range(0, len(vetor)):
        menor = i

        for direita in range(i + 1, len(vetor)):
            if vetor[direita] < vetor[i]:
                menor = direita

        vetor[i], vetor[menor] = vetor[menor], vetor[i]

def InsertionSort(vetor):
    for i in range(0, len(vetor)):
        atual = vetor[i]

        while i > 0 and vetor[i - 1] > atual:
            vetor[i] = vetor[i - 1]
            i -= 1

        vetor[i] = atual

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
            # filtro = self.values['filtro']
            
            if sort == 'QuickSort':
                start = time.time()
                list2 = QuickSort(lista)

                end = time.time()
                print('Tempo de execução QuickSort: {}'.format(end - start))

            if sort == 'BubbleSort':
                start = time.time()
                BubbleSort(lista)
                end = time.time()
                print('Tempo de execução BubbleSort: {}'.format(end - start))

            if sort == 'MergeSort':
                start = time.time()
                Sort(lista)
                end = time.time()
                print("Tempo decorrido MergeSort: {}".format(end - start))

            if sort == 'SelectionSort':
                start = time.time()
                SelectionSort(lista)
                end = time.time()
                print("Tempo decorrido SelectionSort: {}".format(end - start))

            if sort == 'InsertionSort':
                start = time.time()
                InsertionSort(lista)
                end = time.time()
                print("Tempo decorrido InsertionSort: {}".format(end - start))

            if sort == 'Todos':
                start = time.time()
                QuickSort(lista)
                end = time.time()
                print("Tempo decorrido QuickSort: {}".format(end - start))

                start = time.time()
                Sort(lista)
                end = time.time()
                print("Tempo decorrido MergeSort: {}".format(end - start))

                start = time.time()
                InsertionSort(lista)
                end = time.time()
                print("Tempo decorrido InsertionSort: {}".format(end - start))

                start = time.time()
                SelectionSort(lista)
                end = time.time()
                print("Tempo decorrido SelectionSort: {}".format(end - start))

                start = time.time()
                BubbleSort(lista)
                end = time.time()
                print("Tempo decorrido BlubbleSort: {}".format(end - start))

tela = TelaPython()
tela.Iniciar()


#     def pesquisa_binaria(A, item):
#         """Implementa pesquisa binária iterativamente."""
#         esquerda, direita = 0, len(A) - 1
#         while esquerda <= direita:
#             meio = (esquerda + direita) // 2
#             if A[meio] == item:
#                 return meio
#             elif A[meio] > item:
#                 direita = meio - 1
#             else:  # A[meio] < item
#                 esquerda = meio + 1
#         return -1


# print(pesquisa_binaria(lista2,0))
