def next(a,i):
    if a<=i:
        a = a-i
    elif a<0:
        a = i+a
    return f'{a}'

a,i = map(int,input().split())
print(next(a,i))