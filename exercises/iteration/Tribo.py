from math import log
n = int(input())

for i in range(n):
    if n>1:
        if i%1==i:
            i=i**2
            print(i)
        elif log(i)%log(2)==1:
            i=bin(i)
            print(i)