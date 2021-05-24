def multi(lista):
    new_list = []
    x = int(input())
    for element in lista:
        element=element*x
        new_list.append(element)
    print(new_list)
    
x = [int(x) for x in input().split()]
multi(x)