from collections import deque
d=deque()
n=int(input())
for _ in range(n):
    s=input().split()
    if s[0]=='append':
        d.append(s[1])
    elif s[0]=='pop':
        d.pop()
    elif s[0]=='appendleft':
        d.appendleft(s[1])
    elif s[0]=='popleft':
        d.popleft()
        
print(*d)



from collections import deque

d = deque()

for _ in range(int(input())):
    op, *args = input().rsplit()
    getattr(d, op)(*args)

print(*d)
    
