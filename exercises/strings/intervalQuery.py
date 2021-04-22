q =int(input())

for i in range(q):
    l,r,s =input().split()
    l = int(l)
    r = int(r)+1
    sub_string=s[l:r]
    print(sub_string)