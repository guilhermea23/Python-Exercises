def older(ageA, ageB):
    if a>b:
        print("A")
    elif b>a:
        print("B")
    else:
        print("Maybe twins")
        
    
a,b = map(int, input().split())
older(a,b)
