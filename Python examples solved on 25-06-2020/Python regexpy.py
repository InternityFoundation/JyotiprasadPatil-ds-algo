import re
t = int(input())
for i in range(t):
    try :
        s = input()
        re.compile(s)
    except:
        print("False")
        continue
    print("True")





