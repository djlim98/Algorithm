n=int(input())
arr=[]
for i in range(n):
    arr.append(tuple(map(int,input().split(' '))))
arr=sorted(arr,key=lambda x:x[0])
arr=sorted(arr,key=lambda x:x[1])
last=0
count=0
for i in arr:
    if last<=i[0]:
        count+=1
        last=i[1]
print(count)