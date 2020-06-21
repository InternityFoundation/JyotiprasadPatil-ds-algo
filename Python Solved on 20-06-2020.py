# Mod Divmod
a = int(input())
b = int(input())
print(a//b)
print(a%b)
print((divmod(a,b)))


#Mod Power
a = int(input())
b = int(input())
m = int(input())
print(pow(a,b))
print(pow(a,b,m))

#Large Sums
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(pow(a,b)+pow(c,d))

# Coding Contest Maximum problem
size  =int(input())
lst = []
lst1 = []
maxi = 0
for i in range(0,size):
    element = int(input())
    lst.append(element)
for k in range(0,len(lst)):
    for j in range(k+1,len(lst)):
        prod = lst[k]*lst[j]
        maxi = max(prod,maxi)

print(maxi)


# Longest Common Subsequence
string1 = input()
string2 = input()
i = 0
j = 0
def lcs(string1,string2,i,j):
    if (i == len(string1) or j == len(string2)):
        return 0 
    elif (string1[i] == string2[j]):
        return 1+lcs(string1,string2,i+1,j+1)
    else:
        return max(lcs(string1,string2,i+1,j),lcs(string1,string2,i,j+1))

print(lcs(string1,string2,i,j))

 

 # Number of ways
 def helperfunc(info, k):
    if k == 0:
        return 1
    s = len(info) - k
    if info[s] == '0':
        return 0
    
    result = helperfunc(info, k-1)
    if k>=2 and int(info[s:s+2]) <= 26:
        result += helperfunc(info, k-2)
    return result

def num_ways(info):
    return helperfunc(info, len(info))
string = input()
print (num_ways(string))