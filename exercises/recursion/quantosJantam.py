def quantosJantam(n, g, f, c):
    if c==0:
        total = (g+f)//2
        print(total)
    elif g%2==0 or f%2==0:
        total = ((g//2)+(f//2)+(c))
        print(total)
    elif c>0:
        total = ((g//2)+(f//2)+(c)) # 12 0 1 7 rodou
        print(total)
    
    
n,g,f,c = map(int, input().split())
quantosJantam(n,g,f,c)
