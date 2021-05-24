def soma_aninhada(lista):
    soma=0
    for i in lista:
        if type(i) == list:
            soma+=soma_aninhada(i)
        else:
            soma+=i
    return soma