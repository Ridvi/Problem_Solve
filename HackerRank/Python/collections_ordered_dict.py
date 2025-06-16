from collections import OrderedDict

d=OrderedDict()
n=int(input())

for _ in range(n):
    i=input().split()
    item_name=i[:-1]
    item_name=' '.join(item_name)
    price=int(i[-1])
    if item_name in d:
        d[item_name]+=price
    else:
        d[item_name]=price

  
for name,net_price in d.items():
    print(f'{name} {net_price}')
