import math
def areaInstrumento(n,m,r):
    areaNathan = n*m
    areaGustavo = (r**2)* math.sqrt(3)/4
    soma = areaNathan + areaGustavo
    return soma
    

n,m,r = map(int,input().split())
print("{0:.5f}".format(areaInstrumento(n,m,r)))