
def Insertionsort(vetor):
    for i in range(0, len(vetor)):
        atual = vetor[i]

        while i > 0 and vetor[i - 1] > atual:
            vetor[i] = vetor[i - 1]
            i = i- 1

        vetor[i] = atual

    