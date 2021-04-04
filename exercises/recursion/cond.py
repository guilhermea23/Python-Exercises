def cond(p,q,r):
    p = bool(p)
    q = bool(q)
    r = bool(r)
    if p and q==True r==False:
        return False
    else:
        return True
    

p,q,r = input().split()
print(cond(p,q,r))