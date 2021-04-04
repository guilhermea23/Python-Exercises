from math import gcd

n1,n2 = map(int, input().split())
if gcd(n1,n2)==1:
    print("Sao co-primos.")
else:
    print("Nao sao co-primos!")