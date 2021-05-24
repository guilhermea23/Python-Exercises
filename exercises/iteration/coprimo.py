from math import gcd

n1,n2 = map(int, input().split())
if gcd(n1,n2)==1:
    print("Are co-primes.")
else:
    print("Aren't co-primes!")
