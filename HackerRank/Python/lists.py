
N = int(input())
l=[]
for i in range(N):
    command=input().split()
    if command[0]=='insert':
        i=int(command[1])
        e=int(command[2])
        l.insert(i,e)
    elif command[0]=='print':
        print(l)
    elif command[0]=='remove':
        e=int(command[1])
        l.remove(e)
    elif command[0]=='append':
        l.append(int(commaand[1]))
    elif command[0]=='reverse':
        l.reverse()
    elif command[0]=='pop':
        l.pop()
    else:
        l.sort()
        
