from collections import OrderedDict
order_list  =OrderedDict()
n = int(input())
for i in range(n):
    name,space,price = input().rpartition(' ')
    if name not in order_list:
        order_list[name] = int(price)
    else:
        order_list[name] += int(price)
for item_name, net_price in order_list.items():
    print(item_name,net_price)

