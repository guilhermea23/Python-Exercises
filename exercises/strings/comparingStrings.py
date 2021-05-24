a = input()
b = input()
op = 0
if a == b:
    print(op)

elif a!=b:
    op = len(a)//len(b)
    print(op)

elif b!=a:
    op = len(b)+len(a)
    print(op)
        