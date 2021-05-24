import os

nomeDoArquivo = input().split()[-1]

if os.path.isfile(nomeDoArquivo) == True:
    print('O arquivo existe')
else:
    print('Arquivo inexistente')