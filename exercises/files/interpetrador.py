nomeDoArquivo = input()

with open(nomeDoArquivo,'r') as file:
    x=0
    for linha in file:
        if 'a' in linha:
            soma = linha.split('\t')
            soma = soma[1]
            x+=int(soma)
        elif 'b' in linha:
            print(x)