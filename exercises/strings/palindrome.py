entrance = input().lower()
inverse = entrance[::-1]

if entrance == inverse:
    print("Yeah bro!\nIt's valid!")
else:
    print("Shit!\nIt's not valid!")
    