def Quicksort(array):
    menor = []
    igual = []
    maior = []

    if len(array) > 1:
        pivo = array[0]
        for x in array:
            if x < pivo:
                menor.append(x)
            if x == pivo:
                igual.append(x)
            if x > pivo:
                maior.append(x)
      
        return Quicksort(menor)+igual+Quicksort(maior)  

    else:  
        return array
