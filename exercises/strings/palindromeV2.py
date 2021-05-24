entry = input().lower()
inverse = entry[::-1]
i = 0
if len(entry)%2==0:
    if entry[i:] == inverse[i:]:
        print("OFF")
    else:
        print("ON")
