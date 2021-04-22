s = input()
values = []
for letter in s:
    value = ord(letter)
    values.append(value)
added = sum(values)
print(added)