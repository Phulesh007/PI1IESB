# import time
# import psutil




#palavras = arquivo.readlines()

# arquivo = open('TESTBUSCA2.txt',encoding="utf8")
# nomes = []


# for linha in arquivo.readlines():
    
#     palavras = linha.split(';')
#     nomes.append(palavras[0])

from Cidade import Cidade
from collections import defaultdict
from bubble import Bubblesort
from quick import Quicksort
from merge import Mergesort
from insertion import Insertionsort
from selection import Selectionsort
import funcao
import time


arquivo = open('dataSetFinal250k.txt',"r")

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

aux = []
aux2 = []

funcao.retornalistapopulacao(bagulhosImportantes,aux)  

start = time.time()
aux2 = Quicksort(aux)
end = time.time()

print("tempo de ordenação com quick sort : {}".format(end - start))
aux.clear()
#***********************
funcao.retornalistapopulacao(bagulhosImportantes,aux)                  

start = time.time()
Mergesort(aux)
end = time.time()

print("tempo de ordenação com merge sort : {}".format(end - start))
aux.clear()
#*****************
funcao.retornalistapopulacao(bagulhosImportantes,aux)  
start = time.time()
Insertionsort(aux)
end = time.time()

print("tempo de ordenação com insertion sort : {}".format(end - start))
aux.clear()
#***********************
funcao.retornalistapopulacao(bagulhosImportantes,aux)  
start = time.time()
Selectionsort(aux)
end = time.time()

print("tempo de ordenação com selection sort : {}".format(end - start))
aux.clear()
#****************~
funcao.retornalistapopulacao(bagulhosImportantes,aux)  
start = time.time()
Bubblesort(aux)
end = time.time()

print("tempo de ordenação com bubble sort : {}".format(end - start))
aux.clear()    















# for item in bagulhosImportantes["SP"]["São Paulo"]:
#     print(item)
#     print(item.data)
    

# for item in bagulhosImportantes.keys():
#     #print(item, " :************************************************************* ")
#     for item2 in bagulhosImportantes[item].keys():
#         #print(item2, "\t : ")
#         #for item3 in bagulhosImportantes[item][item2]:
            
#         vetci.append(item2)

    
