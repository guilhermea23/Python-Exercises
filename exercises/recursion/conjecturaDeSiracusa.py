def maravilhosos(x):
    if x==1:
        return 1
    elif x%2==0:
        x=x//2
        print(x)
        maravilhosos(x)
    else:
         x=((3*x)+1)
         print(x)
         maravilhosos(x)
    

n = int(input())
print(n)
maravilhosos(n)