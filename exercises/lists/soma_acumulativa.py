def soma_elementos(lista):
    total = 0
    somas=[]
    for i in lista:
       total = total + i
       somas.append(total)
    print(*somas,sep=" ")

x = [int(x) for x in input().split()]
soma_elementos(x)