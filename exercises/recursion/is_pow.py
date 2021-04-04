from math import log
def acredita(n1,n2):
    div = log(n1)/log(n2)
    if n2**div==n1:
        return "Pode Acreditar"
    else:
        return "Fake News"

n1,n2 = map(int,input().split())
print(acredita(n1,n2))