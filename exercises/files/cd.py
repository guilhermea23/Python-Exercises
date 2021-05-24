# import os
# import platform
import sys
# def menu():
#     route = input(" Insira o nome da pasta em que deseja realizar a operação: ")
#     file = input(' Insira a extensão dos arquivos a serem procurados:\n pdf,txt,csv\n')
#     list_of_files(route,file)
#     persist = input("Deseja conferir mais alguma pasta? (s/n)")
#     return persist
# def despedida():
#     print(f"\n\tAté a próxima {platform.uname().node.split('-')[0]}!")
# def list_of_files(route,file):
#     """Retorna a lista dos arquivos do diretório com a extensão fornecida."""
#     path=route
#     ext='.'+file
# 
#     arquivos = []
#     caminhos = []
#     if os.path.isdir(path):
#         with os.scandir(path) as iterador:
#             for item in iterador:
#                 if item.is_file() and item.name.endswith(ext):
#                     arquivos.append(item.name)
#                     caminhos.append(item.path)
#             if len(arquivos)>=1:
#                 print(f"\n Exists {len(arquivos)} file with the extension '{ext}'.\n")
#                 for nome,caminho in zip(arquivos,caminhos):
#                     print(f" Name: {nome}\n Route: {caminho}\n")
#             else:
#                 print(Exception(f"\n Not find files with {ext}"))
# res = 'sS'
# continua = menu()
print(sys.getprofile())
# if continua not in res:
#     despedida()
