import csv
import time

with open('Arquivo/casos_full2.csv') as arquivo_csv:

    lista2 = []
    opcao = 100
    lista = []

    def ler_arquivo():
        leitor = csv.reader(arquivo_csv, delimiter=';')

        
        for [cidade, data, populacao, populacao_2019, casos_confirmado, casos_confirmados_100k, ultima_data, ultima_taxa_mortes, ultimas_mortes, estado, novos_confirmados, novas_mortes] in leitor:

            # print ('{} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {} - {}'.format(cidade, data, populacao, populacao_2019, casos_confirmado, casos_confirmados_100k, ultima_data, ultima_taxa_mortes, ultimas_mortes, estado, novos_confirmados, novas_mortes))
            # print(cidade)
            aux = int(novas_mortes)
            lista.append(aux)

    def pesquisa_binaria(A, item):
        """Implementa pesquisa binária iterativamente."""
        esquerda, direita = 0, len(A) - 1
        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            if A[meio] == item:
                return meio
            elif A[meio] > item:
                direita = meio - 1
            else:  # A[meio] < item
                esquerda = meio + 1
        return -1

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

    def SelectionSort(vetor):
        for i in range(0, len(vetor)):
            menor = i

            for direita in range(i + 1, len(vetor)):
                if vetor[direita] < vetor[i]:
                    menor = direita

            vetor[i], vetor[menor] = vetor[menor], vetor[i]

    def BubbleSort(vetor):
        for final in range(len(vetor), 0, -1):
            flag = False

            for i in range(0, final - 1):
                if vetor[i] > vetor[i + 1]:
                    vetor[i + 1], vetor[i] = vetor[i], vetor[i + 1]
                    flag = True

            if flag == True:
                break

    def InsertionSort(vetor):
        for i in range(0, len(vetor)):
            atual = vetor[i]

            while i > 0 and vetor[i - 1] > atual:
                vetor[i] = vetor[i - 1]
                i -= 1

            vetor[i] = atual


    # list = [54,26,93,17,77,31,44,55,20]

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
            #  There's no left element to be processed
            # nada para ser processado a esquerda
            if i > ifim:
                aux[p] = vetor[j]
                j += 1

            #  There's no right element to be processed
            # nada para ser processado a direita
            elif j > jfim:
                aux[p] = vetor[i]
                i += 1

            #  Compare left with right
            # compara esquerda com direita
            elif vetor[i] < vetor[j]:
                aux[p] = vetor[i]
                i += 1

            else:
                aux[p] = vetor[j]
                j += 1

        for k in range(start, end + 1):
            vetor[k] = aux[k]

    # Sort(list)

    # Funções do programa
    def menu_funcs():
        print("""
                Escolha uma opção:
                (1) = Ordenar com QuickSort 
                (2) = Ordenar com MergeSort
                (3) = Ordenar com InsertioSort
                (4) = Ordenar com SelectionSort
                (5) = Ordenar com BlubbleSort
                (6) = Comparação entre os algoritmos
                (0) = Para SAIR
        """)

    # menu_funcs()

        opcao = int(input("Qual a opção desejada? "))
        if opcao == 1:
            ler_arquivo()
            start = time.time()
            lista2 = QuickSort(lista)
            end = time.time()
            print(lista2)
            print(end - start)
            menu_funcs()

        if opcao == 2:
            ler_arquivo()
            start = time.time()
            Sort(lista)
            print(lista)
            end = time.time()
            print(end - start)
            menu_funcs()
        
        if opcao == 3:
            ler_arquivo()
            start = time.time()
            InsertionSort(lista)
            print(lista)
            end = time.time()
            print(end - start)
            menu_funcs()
        
        if opcao == 4:
            ler_arquivo()
            start = time.time()
            SelectionSort(lista)
            print(lista)
            end = time.time()
            print(end - start)
            menu_funcs()
        
        if opcao == 5:
            ler_arquivo()
            start = time.time()
            BubbleSort(lista)
            print(lista)
            end = time.time()
            print(end - start)
            menu_funcs()

        if opcao == 6:
            ler_arquivo()
            start = time.time()
            QuickSort(lista)
            end = time.time()
            print("Tempo decorrido QuickSort: {}".format(end - start))

            ler_arquivo()
            start = time.time()
            Sort(lista)
            end = time.time()
            print("Tempo decorrido MergeSort: {}".format(end - start))

            ler_arquivo()
            start = time.time()
            InsertionSort(lista)
            end = time.time()
            print("Tempo decorrido InsertionSort: {}".format(end - start))

            ler_arquivo()
            start = time.time()
            SelectionSort(lista)
            end = time.time()
            print("Tempo decorrido SelectionSort: {}".format(end - start))

            ler_arquivo()
            start = time.time()
            BubbleSort(lista)
            end = time.time()
            print("Tempo decorrido BlubbleSort: {}".format(end - start))

        if opcao == 0:
            quit()

    menu_funcs()
# print(pesquisa_binaria(lista2,0))
