
def certeza(a,b,c):
    interable = 0
    if a==b and a!=0 and b!=0:
        interable+=1
    elif a==c and a!=0 and c!=0:
        interable+=1
    elif b==c and b!=0 and c!=0:
        interable+=1
        
    return interable
        
    

n = int(input())
results=[]
for i in range(n):
    a,b,c = map(int,input().split())

    result = certeza(a,b,c)
    results.append(result)

print(sum(results))