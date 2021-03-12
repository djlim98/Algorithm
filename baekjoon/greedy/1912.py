n=int(input())
arr=list(map(int,input().split(' ')))
sum1=arr[0]
result=arr[0]
for i in range(n-1):
    temp=max(sum1+arr[i+1],arr[i+1])
    sum1=temp
    result=max(result,temp)
print(result)