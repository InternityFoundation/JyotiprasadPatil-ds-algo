from itertools import combinations

s,n = input().split()

for l in range(1,int(n)+1):
    for a in combinations (sorted(s),l):
        print(''.join(a))
