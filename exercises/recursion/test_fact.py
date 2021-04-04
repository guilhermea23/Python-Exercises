import math
def factorial(n):
    if n < 2:
        print(1)
    else:
        fact = n * math.factorial(n-1)
        print(fact)
        
n =int(input())
factorial(n)
