def maior_norma(l1,l2):
    sum1=0
    sum2=0
    for e in l1:
        sum1+=e
    for el in l2:
        sum2+=el
    
    if sum1>sum2:
        print("PRIMEIRO")
    elif sum2<=sum1:
        print("SEGUNDO")

i=0
l1=[]
l2=[]
l1 = [int(x) for x in input().split()]
l2=[int(z) for z in input().split()]
    
maior_norma(l1,l2)