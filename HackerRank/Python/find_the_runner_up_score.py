n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
c=arr.count(arr[0])
large=arr[0]
for i in range(c):
    arr.remove(large)
    
print(arr[0])
