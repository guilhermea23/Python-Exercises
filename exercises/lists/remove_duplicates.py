def remove_duplicatas(lista):
    for e in lista:
        counter = lista.count(e)
        if counter!=1:
            lista.remove(e)
            new_lista = lista.copy()
            new_lista=sorted(new_lista)
            counter-=1
    return new_lista
        
        
x = [i for i in input().split(",")]
print(remove_duplicatas(x))