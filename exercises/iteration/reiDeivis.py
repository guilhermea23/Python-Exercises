n = int(input())

i=0
doa = 0
total = []
for i in range(n):
    qtdDinheiro = int(input())
    total.append(qtdDinheiro)
    if qtdDinheiro<1000:
        doa+=1
    else:
        pass
res = (1000%sum(total))//doa
print(res)