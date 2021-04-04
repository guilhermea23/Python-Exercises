def fib(n):
    ident = ' ' * n     # identacao para auxiliar a visualizacao
    print(ident, 'fib', n)
    if n < 1:
        print(ident, 'retorna', 0)
        return 0
    elif n == 1:
        print(ident, 'retorna', 1)
        return 1
    else:
        res = fib(n-1) + fib(n-2)
        print(ident, 'retorna', res)
        return res
    
n = int(input())
fib(n)
