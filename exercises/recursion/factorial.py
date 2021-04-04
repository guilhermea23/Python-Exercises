"""
Considere o cálculo do fatorial de um número:
n!=n⋅(n−1)⋅(n−2)⋅…⋅3⋅2⋅1
Para implementar uma função recursiva que calcule o fatorial de um número n qualquer (n≥0), considere o caso mais simples, quando n tem o menor valor (0). Neste caso, nenhum processo é necessário pois sabe-se que a resposta é 1. Portanto, o caso base é definido como:

se n
for 0, retorne 1.
_________________________________________________________________
Considerando o próximo caso mais simples, e assim sucessivamente:

    1!=1⋅0!=1

  (0! é o caso base)
2!=2⋅1!=2
  (1! é o caso anterior) 
3!=3⋅2!=6
  (2! é o caso anterior)
⋮
10!=10⋅9!=3628800

     (9! é o caso anterior)

Portanto, para todo n>0, o processo pode ser descrito como
n!=n⋅(n−1)!
_________________________________________________________________
Resposta:

"""


def fatorial(n):
    n=int(n)
    if n <= 1: # caso base
        factorial = 1
        return factorial
    else:
        factorial = n*fatorial(n-1)
        return factorial
