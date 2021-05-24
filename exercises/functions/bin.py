def binario(num):
  num = int(num)
  return print(bin(num))


numbers = [x for x in input().split()]
for n in numbers:
  binario(n)
