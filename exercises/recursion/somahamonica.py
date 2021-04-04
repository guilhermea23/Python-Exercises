def soma_harmonica(X):
    if X ==1:
        return 1
    elif X!=0 and X>1:
        soma = (1/X)+soma_harmonica(X-1)
        return soma

x=int(input())
print(soma_harmonica(x))