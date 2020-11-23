import time
nomes = []

arquivo = open('TESTBUSCA2.txt',encoding="utf8")

#palavras = arquivo.readlines()

for linha in arquivo.readlines():
    
    palavras = linha.split('\n')
    nomes.append(palavras[0])

teste = input("digite uma palavra: ")

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


# elif A[meio] > item:
#     direita = meio - 1
# else: # A[meio] < item
#     esquerda = meio + 1
start = time.time()
print(pesquisa_binaria(nomes,teste))
end = time.time()
print("tempo de busca com busca binaria : {}".format(end - start))



start = time.time()
for i in range(len(nomes)):
    #print(i)
    if nomes[i].lower() == teste.lower():
        print(i)
        end = time.time()
        break

print("tempo de busca com busca sequencial : {}".format(end - start))
    