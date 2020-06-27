n = int(input())
lst = []
for i in range(0,n):
    elem = int(input())
    lst.append(elem)
len1 = len(lst)

if len1 == 0:
    print(0)
if len1 == 1:
    print(lst[0])
if len1 == 2:
    print(max(lst[0],lst[1]))

dp = [0]*n
dp[0] = lst[0]
dp[1] = max(lst[0],lst[1])
for i in range(2, n):
    dp[i] = max(lst[i]+dp[i-2], dp[i-1])

print(dp[-1])