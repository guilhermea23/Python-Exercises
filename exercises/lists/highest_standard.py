def highest_standard(l1,l2):    
    if sum(l1)>sum(l2):
        print("FIRST")
    else:
        print("SECOND")

l1 = [int(x) for x in input().split()]
l2=[int(z) for z in input().split()]
    
highest_standard(l1,l2)
