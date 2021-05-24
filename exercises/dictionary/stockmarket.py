def stockmarket(x):
    d = {}
    for i in x:
        if i[0] not in d:
            d[i[0]] = float(i[1]*i[2])
        else:
            d[i[0]] += i[1]*i[2]
    return d

datas = {}
date,price, n = input().split()
datas[date] = price/n