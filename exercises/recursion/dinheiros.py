"""
O grande Fibonacci percebeu um padrão numérico recorrente, e propôs a sequência de Fibonacci (com inúmeras aplicações!). Uma versão dessa lenda é que a sequência responde à milenar pergunta: se abandonarmos um casal de coelhos recém nascidos em um campo qualquer, quantos pares de coelhos haveriam em N ≥ 0 meses?

O detalhe é que a situação tem algumas condições:
os coelhos de Fibonacci podem reproduzir a partir de 1 mês de idade;
o período de gestação de um coelho é de 1 mês;
cada gestação produz um novo casal de coelhos;
coelhos são imortais!
A resposta para a pergunta pode ser obtida com uma função recursiva!
"""
def fib(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

n=int(input())
fibonacci = fib(n)
print(fibonacci)