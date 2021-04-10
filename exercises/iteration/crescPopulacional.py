popA,popB,cresA,cresB = input().split()

popA = int(popA)
popB = int(popB)
cresA = float(cresA)
cresB = float(cresB)

if popA < popB:
    tempo = (popB - popA)//(cresB-cresA)
print(int(tempo))