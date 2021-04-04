def nota(peso1,peso2,peso3,mencao,nota1,nota2):
    nota1 = int(nota1)
    nota2 = int(nota2)
    peso1 = int(peso1)
    peso2 = int(peso2)
    peso3 = int(peso3)
    if mencao =="MM":
        des = 5
        media = ((nota1*peso1)+(nota2*peso2)+(peso3))//((peso1+peso2+peso3))
        return media+des
    elif mencao =="MS":
        media=(((nota1*peso1)+(nota2*peso2)+(peso3))//((peso1+peso2+peso3))*7)
        return media
    else: #SS
        media=((nota1*peso1)+(nota2*peso2)+(10*peso3))//(peso1+peso2+peso3)
        return media
        

p1,p2,p3,M,n1,n2 = input().split()
print(nota(p1,p2,p3,M,n1,n2))