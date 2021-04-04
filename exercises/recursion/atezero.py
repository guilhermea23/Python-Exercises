def ate_zero(numero):
    if numero >= 0:
        if numero<10:
            print("0"+str(numero))
            ate_zero(numero-1)
        else:
            print(numero)
            ate_zero(numero-1)

n = int(input())
ate_zero(n)
