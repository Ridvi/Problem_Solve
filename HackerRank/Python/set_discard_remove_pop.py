n = int(input())
s = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    command=input().split()
    comm=command[0]
    
    if comm=='pop':
        s.pop()
        
    elif comm=='remove':
        try:
            s.remove(int(command[1]))
        except:
            print('no matched element found')
    
    elif comm=='discard':
        s.discard(int(command[1]))
        
print(sum(s))       
            
        
