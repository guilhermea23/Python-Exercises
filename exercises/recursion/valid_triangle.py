def valid_triangle(a,b,c):
    if (a <(b+c)) and (a >(b-c)):
        if (b<(a+c)) and (b>(a-c)):
            if (c<a+b) and (c>(a-b)):
                print("valido")
            else:
                print("invalido")
        else:
            print("invalido")
    else:
        print("invalido")

a,b,c = map(int, input().split())
valid_triangle(a,b,c)
