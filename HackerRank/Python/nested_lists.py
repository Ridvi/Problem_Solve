l=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name,score])
    

l.sort(key=lambda x:x[1])

for i in range(len(l)):
    if l[i][1]<l[i+1][1]:
        second_smallest=l[i+1][1]
        break
        
name_list=[]       
for i in range(len(l)):
    if l[i][1]==second_smallest:
        name_list.append(l[i][0])
    elif second_smallest<l[i][1]:
        break
        
name_list.sort()
print('\n'.join(name_list))
