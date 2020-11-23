def retornalistamortos(bagulhosImportantes,vet):
    for item in bagulhosImportantes.keys():
            for item2 in bagulhosImportantes[item].keys():
                for item3 in bagulhosImportantes[item][item2]:
                    vet.append(item3.ultimas_mortes)

def retornalistapopulacao(bagulhosImportantes,vet):
    for item in bagulhosImportantes.keys():
            for item2 in bagulhosImportantes[item].keys():
                for item3 in bagulhosImportantes[item][item2]:
                    vet.append(item3.ultimas_mortes)

def retornalistacasos(bagulhosImportantes,vet):
    for item in bagulhosImportantes.keys():
            for item2 in bagulhosImportantes[item].keys():
                for item3 in bagulhosImportantes[item][item2]:
                    vet.append(item3.ultimas_mortes)                    
