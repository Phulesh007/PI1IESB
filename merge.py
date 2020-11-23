list = [54,26,93,17,77,31,44,55,20]

def Mergesort(vetor):
    aux = vetor[:]
    mergesort2(vetor, aux, 0, len(vetor) - 1)


def mergesort2(vetor, aux, start, end):
    if start >= end:
        return

    meio = (start + end) // 2

    mergesort2(vetor, aux, start, meio)
    mergesort2(vetor, aux, meio + 1, end)

    ordena(vetor, aux, start, end)


def ordena(vetor, aux, start, end):
    i = start
    ifim = (start + end) // 2

    j = ifim + 1
    jfim = end

    for p in range(start, end + 1):
        #  There's no left element to be processed
        if i > ifim:
            aux[p] = vetor[j]
            j += 1

        #  There's no right element to be processed
        elif j > jfim:
            aux[p] = vetor[i]
            i += 1

        #  Compare left with right
        elif vetor[i] < vetor[j]:
            aux[p] = vetor[i]
            i += 1

        else:
            aux[p] = vetor[j]
            j += 1

    for k in range(start, end + 1):
        vetor[k] = aux[k]
