n = int(input())
i=0
nums = []
for i in range(n):
    num1 = int(input())
    nums.append(num1)

nums.sort()
maior = nums[-1] 
menor = nums[0]
print(f"Menor: {menor}\nMaior: {maior}")
