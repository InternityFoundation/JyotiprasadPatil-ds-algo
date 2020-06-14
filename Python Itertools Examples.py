#Python itertools.product

from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(*product(a,b))


#Python itertools.permutations
from itertools import permutations

s,n = input().split()
n = int(n)
output = ["".join(i) for i in permutations(s,n)]
output.sort()
print("\n".join(output))

#Python Polar Coordinates
import cmath
print(*cmath.polar(complex(input())), sep='\n')


#Python itertools.combinations()
from itertools import combinations

s,n = input().split()

for l in range(1,int(n)+1):
    for a in combinations (sorted(s),l):
        print(''.join(a))

