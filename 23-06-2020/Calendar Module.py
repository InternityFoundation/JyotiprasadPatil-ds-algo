
import calendar
input1 = input().split()
month = int(input1[0])
day = int(input1[1])
year = int(input1[2])
c = calendar.weekday(year, month, day)
if c == 0:
    print("MONDAY")
elif c == 1:
    print("TUESDAY")
elif c == 2:
    print("WEDNESDAY")
elif c==3:
    print("THURSDAY")
elif c==4:
    print("FRIDAY")
elif c== 5:
    print("SATURDAY")
elif c==6:
    print("SUNDAY")
