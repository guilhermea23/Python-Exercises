def binario(num):
  num = int(num)
  print(bin(num))


numbers = [x for x in input().split()]
for n in numbers:
  binario(n)
