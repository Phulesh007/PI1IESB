def Selectionsort(vetor):
    for i in range(0, len(vetor)):
        menor = i

        for direita in range(i + 1, len(vetor)):
            if vetor[direita] < vetor[i]:
                menor = direita

        vetor[i], vetor[menor] = vetor[menor], vetor[i]