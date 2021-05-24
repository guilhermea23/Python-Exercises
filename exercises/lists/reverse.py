entry = [int(x) for x in input().split()]
if entry[-1]<0.0:
    entry.remove(entry[-1])
    entry.reverse()
    print(*entry, sep=" ")
