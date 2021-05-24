name = input()

with open(name,'r',encoding='utf-8') as file:
    linhas = file.read()
    print(linhas.replace(",",";"))
