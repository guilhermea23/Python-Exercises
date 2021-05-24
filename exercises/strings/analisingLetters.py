import math
rna1 = input()
rna2 = input()

size1 = len(rna1)
size2 = len(rna2)
counter = 0
i = 0

if rna1[i]!=rna2[i]:
    counter+=1
    
print(counter)