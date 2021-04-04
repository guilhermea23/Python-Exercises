def print_rectangle(a,b,c):
    ao = a-4
    print(a)
    print("x"*a)
    print("x"," "*ao,"x")
    print("x"," "*ao,"x")
    print("x"*a)
    bo = b-4
    print(b)
    print("x"*b)
    print("x"," "*bo,"x")
    print("x"," "*bo,"x")
    print("x"*b)
    co = c-4
    print(c)
    print("x"*c)
    print("x"," "*co,"x")
    print("x"," "*co,"x")
    print("x"*c)
    

a,b,c = map(int,input().split())
print_rectangle(a,b,c)
