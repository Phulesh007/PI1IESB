import csv

with open('Arquivo/casos_full2.csv') as arquivo_csv:

    leitor = csv.reader(arquivo_csv, delimiter=';')

    lista = []
    lista2 = []
    opcao = 100

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

    # Funções do programa
    def menu_funcs():
        print("""
                Escolha uma opção:
                (1) = Ordenar com QuickSort 
                (2) = Ordenar com MergeSort
                (3) = Ordenar com BlubbleSort
                (4) = Ordenar com InsertionSort
                (5) = Ordenar com SelectionSort
                (0) = Para SAIR
        """)

    # menu_funcs()

        opcao = int(input("Qual a opção desejada? "))
        if opcao == 1:
            lista2 = qsort(lista)
            print(lista2)
            menu_funcs()

        if opcao == 2:
        
        if opcao == 3:
        
        if opcao == 4:
        
        if opcao == 5:

        if opcao == 0:
            quit()

    menu_funcs()
# print(pesquisa_binaria(lista2,0))
