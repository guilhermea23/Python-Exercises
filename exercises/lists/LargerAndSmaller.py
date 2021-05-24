score = [int(x) for x in input().split()]

smaller = min(score)
bigger = max(score)

i_s = score.index(smaller)
i_b = score.index(bigger)

print(f'{smaller} {i_s}')
print(f'{bigger} {i_b}')
print(*score,sep=" ")
score = sorted(score)
print(*score, sep=" ")
