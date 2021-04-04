def paresDeNumeros(n,m):
    if n<=m:
        print(f'{n} {m}')
        paresDeNumeros(n+1,m-1)
n,m = map(int,input().split())
paresDeNumeros(n,m)