
def Bubblesort(vetor):

    for final in range(len(vetor), 0, -1):
        flag = False

        for i in range(0, final - 1):
            if vetor[i] > vetor[i + 1]:
                vetor[i + 1], vetor[i] = vetor[i], vetor[i + 1]
                flag = True

        if not flag:
            break
