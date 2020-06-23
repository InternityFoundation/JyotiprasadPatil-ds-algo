from collections import defaultdict
d = defaultdict(list)
n,m = map(int, input().strip().split())
[d[ input().strip()].append(str(a)) for a in range(1,n+1)]
for a in range(m):
    f= input().strip()
    if not d[f]:
        print(-1)
        continue
print(' '.join(d[f]))