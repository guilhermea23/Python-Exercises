n = int(input())
i=0
nums = []
for i in range(n):
    num1 = int(input())
    nums.append(num1)

nums.sort()
big = nums[-1] 
little = nums[0]
print(f"Smaller number: {little}")
print(f"Higher number: {big}")
