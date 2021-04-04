def fatorialPeculiar(n):
    if n<2:
        return 1
    elif n%2==0:
        fatorial = fatorialPeculiar(n-1)*(n//2)
    elif n%2!=0:
        fatorial = fatorialPeculiar(n-1)*(n**2)
    
    return fatorial
        

n = int(input())
print(fatorialPeculiar(n))