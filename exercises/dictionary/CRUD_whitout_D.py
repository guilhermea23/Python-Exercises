# Dicionarios são abertos com dict() e possuem chave e valor
# sendo que:
#     a= dict()
#     a= {'chave':'valor'} 

# Inicio do programa
dic_inicial = {
    'João': 10,
    'Maria': 10,
    'Jorge': 4,
    'Marta': 5,
    'Mário': 6,
    'Mikael': 9
}

q = int(input())
old = ["op","nome","nota"]
d=list()
for i in range(q):
    dados = [i for i in input().split()]
    d.append(dict(zip(old,dados)))
for elemento in d:
    if elemento["op"] == "C":
        nome = elemento["nome"]
        nota = elemento["nota"]
        dic_inicial[nome] = nota
    elif elemento["op"] == "R":
        if elemento["nome"] in dic_inicial:
            nome = elemento["nome"]
            nota = dic_inicial[nome]
        print(nome,nota)
    elif elemento["op"] == "U":
        if elemento["nome"] in dic_inicial:
            nome = elemento["nome"]
            dic_inicial[elemento["nome"]] = elemento["nota"]
            nota = elemento["nota"]
