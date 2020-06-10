# Q1. If Else


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print ('Weird')
    elif n%2 == 0 and (n >= 2 and n<=5):
        print ('Not Weird')
    elif n%2 == 0 and (n>=6 and n<=20):
        print ('Weird')
    elif n%2 == 0 and (n>=20):
        print ('Not Weird')


#Q2 Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    sum1 = a+b
    difference = a-b
    product = a*b
    print(sum1)
    print(difference)
    print(product)

#Q3 Python Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#Q4 Python loops
if __name__ == '__main__':
    n = int(input())
    for i in range (0,n):
        print(i*i)

#Q5 Python write a Function
def is_leap(year):
    leap = False
    
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    
    
year = int(input())
print(is_leap(year))

#Q5 Python List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

   
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

#Q6 Find the Runner Up Score
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()
    i = 0
    if arr[i]>arr[i+1]:
        print(arr[i+1])
    elif arr[i]>arr[i+2]:
        print(arr[i+2])
    elif arr[i]>arr[i+3]:
        print(arr[i+3])
    elif arr[i]>arr[i+4]:
        print(arr[i+4])
    elif arr[i]>arr[i+9]:
        print(arr[i+9])   

 #Nested List

 if __name__ == '__main__':
   n = int(input())
students = [[input(), float(input())] for studentrecord in range(n)]

students.sort(key=lambda studentrecord: float(studentrecord[1]))

lowest_mark = students[0][1]

ind = 0
while students[ind][1] == lowest_mark:
    ind += 1

second_lowest_mark = students[ind][1]

second_lowest_scoring_students = []

while students[ind][1] == second_lowest_mark:
    second_lowest_scoring_students.append(students[ind][0])
    ind += 1
    if ind == n: 
        break

second_lowest_scoring_students.sort()

for student_name in second_lowest_scoring_students:
    print(student_name)


#Find the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    n = sum(student_marks[query_name])/3
    print ('%.2f'%n) 

# Tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
# Swap Case
def swap_case(s):
    s = s.swapcase()
    return s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# String Split And Join
def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#String Mutation
def mutate_string(string, position, character):
    string = list(string)
    string[position] = c
    string = ''.join(string)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)