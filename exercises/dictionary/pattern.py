n = int(input())

d= {}
i=0
i+=1
while i<=n:
    if i%2!=0:
        d[i] = i*5
        i+=1
    else:
        d[i] = i**2
        i+=1

print(d)