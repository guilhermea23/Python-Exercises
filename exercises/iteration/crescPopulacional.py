popA,popB,cresA,cresB = input().split()

popA = int(popA)
popB = int(popB)
cresA = float(cresA)
cresB = float(cresB)

if (popA < popB):
    popA = popA - (popA * cresA)
    popB = popB - (popB * cresB)
    tempo = (cresA - cresB)*(popB-popA)
    print(int(tempo))