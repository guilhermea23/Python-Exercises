n = int(input())

i=0
for i in range(n):
    qtdDinheiro = int(input())
    if qtdDinheiro<=1000:
        res = 1000-qtdDinheiro
    elif qtdDinheiro>100:
        res = (1000%qtdDinheiro)
print(res)