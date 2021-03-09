n,k=map(int,input().split(' '))
arr=[]
for i in range(n):
    arr.append(int(input()))
i=len(arr)-1
count=0
while True:
    if 0==k:
        break
    if k>=arr[i]:
        count+= k//arr[i]
        k%=arr[i]
    i-=1
print(count)