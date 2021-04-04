def multiple(a,b):
    if a%b == 0:
        print(f"{a} is multiple of {b}")
    elif b%a == 0:
        print(f"{b} is multiple of {a}")
    else:
        print("not multiples")

a,b = map(int,input().split())
multiple(a,b)