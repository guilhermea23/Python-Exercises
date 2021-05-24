n = int(input())
lista = []
d=dict()
for i in range(n):
    nome,sobrenome = map(str,input().split(":"))
    d[nome] = sobrenome
    lista.append({nome:sobrenome})
    print(lista[-1])

print(d)