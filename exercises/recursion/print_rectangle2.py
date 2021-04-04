def print_rectangle(a,b,c):
    
    if a<4:
        space_a = (4-a)
    else:
        space_a = (a-4)
    print(a)
    print("+"*a)
    print("+"," "*space_a,"+")
    print("+"*a)
    
    if b<4:
        space_b = (4-b)
    else:
        space_b = (b-4)
    print(b)
    print("+"*b)
    print("+"," "*space_b,"+")
    print("+"*b)
    
    if c<4:
        space_c = (4-c)
    else:
        space_c = (c-4)
    print(c)
    print("+"*c)
    print("+"," "*space_c,"+")
    print("+"*c)

a,b,c = map(int,input().split())
print_rectangle(a,b,c)
