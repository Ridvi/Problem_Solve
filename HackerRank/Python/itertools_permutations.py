from itertools import permutations

i=input().split()
s=i[0]
k=int(i[1])

p=sorted(permutations(s,k))

for element in p:
    print(''.join(element))
