n,amount = input().split()
n = int(n)
amount = int(amount)
a = input()
lst = a.split()
new_list = list(map(int,lst))
len1 = len(new_list)
def numberofCoins(new_list,len1,amount):
    if (amount == 0):
        return 0
    result = 10000
    for i in range(0,len1):
        if(new_list[i] <= amount):
            answer = numberofCoins(new_list,len1,amount-new_list[i])


            if(answer != 10000 and answer + 1 < result):
                result = answer + 1

    return answer

print(numberofCoins(new_list,len1,amount))