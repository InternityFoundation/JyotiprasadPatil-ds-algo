#Python Set Examples 
#Set Introduction

def average(array):
    set1 = set(arr)
    sum1 = sum(set1)
    avg1 = sum1/len(set1)
    return avg1

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

#Set Add
print(len(set([str(input()) for x in range(int(input()))])))

#Set Discard Remove and Pop
n = int(input())
s = set(map(int, input().split()))
N = int(input())
d = {"pop":s.pop, "remove":s.remove, "discard": s.discard}
for _ in range(N):
    c = input().split()
    d[c[0]](int(c[1])) if len(c)>1 else d[c[0]]()
print(sum(s))

#Set Union
n = int(input())
s = set(map(int, input().split()))
m =int(input())
s2 = set(map(int, input().split()))
s1 = s.union(s2)
print(len(s1))

#Set Intersection
m = int(input())
s1 = set(map(int, input().split()))
n = int(input())
s2 = set(map(int, input().split()))
s3 = s1.intersection(s2)
print(len(s3))


#Symmetric Difference Problem

m = int(input())
arr1 = input()
list1 = arr1.split()
new_list1 = list(map(int,list1))
n = int(input())
arr2 = input()
list2 = arr2.split()
new_list2 = list(map(int,list1))
set1 = set(list1)
set2 = set(list2)
set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set3.difference(set4)
set5 = list(set5)
set5.sort()
print(set5)
