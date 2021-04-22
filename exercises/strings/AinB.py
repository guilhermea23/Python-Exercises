def confere(x,y):
    if x.endswith(y):
        print("ta dentro!!!")
    else:
        print("ta fora...")
    
a,b = input().split()
confere(a,b)