def anobissexto(a):
    if a%400==0 or a%4==0 and a%100!=0:
        return "Sim"
    else:
        return "Nao"

a = int(input())
print(anobissexto(a))