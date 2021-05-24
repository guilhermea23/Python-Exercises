x,base = map(int, input().split())
nums = [int(i) for i in input().split()]
soma = 0
for n in nums:
    soma+=n*(base**x)
    x-=1

print(soma)