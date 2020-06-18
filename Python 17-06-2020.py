# Set.difference Operation
m = int(input())
a = input()
list1 = a.split()
new_list = list(map(int,list1))
new_list = set(new_list)
n = int(input())
b = input()
list2 = b.split()
new_list1 = list(map(int,list2))
new_list1 = set(new_list1)
answer = new_list.difference(new_list1)
count = 0
for i in answer:
    count = count+1
print(count)


# Set.symmetric_difference Problem
m = int(input())
a = input()
lis1 = a.split()
new_list = list(map(int,lis1))
n = int(input())
b = input()
lis2 = b.split()
new_list1 = list(map(int,lis2))
new_list = set(new_list)
new_list1 = set(new_list1)
answer = new_list.symmetric_difference(new_list1)
count = 0
for i in answer:
    count = count+1
print(count)


# Set Mutations
n = int(input())
a = input()
lis = a.split()
first_list = list(map(int,lis))
first_list = set(first_list)
o = int(input())
for i in range(o):
    s,b = input().split()
    if s == "intersection_update":
        first_list.intersection_update(set(map(int, input().split())))
    elif s == "update":
        first_list.update(set(map(int, input().split())))
    elif s == "symmetric_difference_update":
        first_list.symmetric_difference_update(set(map(int, input().split())))
    else:
        first_list.difference_update( set(map(int, input().split())))
print(sum(first_list))


#Check Subset Problem
t = int(input())
for i in range(t):
    m = int(input())
    a = input()
    lis = a.split()
    new_lis = list(map(int,lis))
    new_lis = set(new_lis)
    n = int(input())
    b = input()
    lis1 = b.split()
    new_lis1 = list(map(int,lis1))
    new_lis1 = set(new_lis1)
    print(new_lis.issubset(new_lis1))


#Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

#One fine day, a finite number of tourists come to stay at the hotel.
#The tourists consist of:
#→ A Captain.
#→ An unknown group of families consisting of  members per group where  ≠ .

#The Captain was given a separate room, and the rest were given one room per group.

#Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.

#Mr. Anant needs you to help him find the Captain's room number.
#The total number of tourists or the total number of groups of families is not known to you.
#You only know the value of  and the room number list.

k = int(input())
a = input()
list1 = a.split()
new_list = list(map(int,list1))
new_list.sort()
l = len(new_list)
for i in range(l):
    if (i == l-1 and new_list[i-1] != new_list[i]) or (i == 0 and new_list[i+1] !=new_list[i]) or (new_list[i+1]!=new_list[i] and new_list[i-1]!=new_list[i]):
        print(new_list[i])