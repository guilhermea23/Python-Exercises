# name = input()
# 
# with open(name,'r',encoding='utf-8') as file:
#     dados = file.read()
#     elemento = [dados.split(',') for x in dados]
#     for dado in elemento:
#         print(int(dado[1]))

name = input()

with open(name,'r',encoding='utf-8') as file:
    dados = file.readlines()
    for dado in dados:
        elemento = dado.split(',')
        elemento = elemento.replace('\n','')
        print(elemento[1])
