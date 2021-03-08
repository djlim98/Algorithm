n=int(input())
arr=list(map(int,input().split(' ')))

arr.sort()
a=0
b=n-1
m=abs(arr[a]+arr[b])
result=[arr[a],arr[b]]

while a<b:
    temp=arr[a]+arr[b]
    if abs(temp)<m:
        m=abs(temp)
        result=[arr[a], arr[b]]
        if m==0:
            break
    if temp<0:
        a+=1
    else:
        b-=1

print(result[0],result[1])