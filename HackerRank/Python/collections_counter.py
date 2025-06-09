from collections import Counter as counter

X=int(input())
sizes=list(map(int,input().split()))
customers=int(input())
frequency=counter(sizes)
total=0
for _ in range(customers):
    size,price=map(int,input().split())
    if frequency[size]>0:
        total+=price
        frequency[size]-=1
    
print(total)
   
    


    
