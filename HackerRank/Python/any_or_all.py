n=int(input())
numbers=list(map(int,input().split()))
result=all(num>0 for num in numbers) and any(str(num)==str(num)[::-1] for num in numbers) #[::-1] for reversing

print(result)
