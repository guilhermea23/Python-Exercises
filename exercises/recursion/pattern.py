def pattern(n):
    if n<=0:
        n+=5
        print(n)
        pattern(n)
    else:
        n-=5
        print(n)
        pattern(n)
n = int(input())
pattern(n)