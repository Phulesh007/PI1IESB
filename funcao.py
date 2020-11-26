def retornalistamortos(bagulhosImportantes,vet):
    for item in bagulhosImportantes.keys():
            for item2 in bagulhosImportantes[item].keys():
                for item3 in bagulhosImportantes[item][item2]:
                    vet.append(item3.ultimas_mortes)

def retornalistapopulacao(bagulhosImportantes,vet):
    for item in bagulhosImportantes.keys():
            for item2 in bagulhosImportantes[item].keys():
                for item3 in bagulhosImportantes[item][item2]:
                    vet.append(item3.populacao)

def retornalistacasos(bagulhosImportantes,vet):
    for item in bagulhosImportantes.keys():
            for item2 in bagulhosImportantes[item].keys():
                for item3 in bagulhosImportantes[item][item2]:
                    vet.append(item3.casos_confirmado)                    

                    
def pesquisa_binaria(A, item):
    

    """Implementa pesquisa binária iterativamente."""
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio].lower() == item:
            return meio
        else:
            aux = A[meio].lower()
            #print(aux)
            for i in range(len(item)):
                if item[i].lower() == aux[i]:
                    continue
                elif item[i].lower() > aux[i]:
                    esquerda = meio + 1
                    break
                else:#item[i] < aux[i]
                    direita = meio -1
                    break


    return -1
