def reverso(n):
    if n>0:
        num = str(n)
        num = num[::-1]
        print(int(num))
    else:
        num = str(n)
        num = num[::-1]
        print("-"+num.replace("-",""))
    
n = int(input())
reverso(n)