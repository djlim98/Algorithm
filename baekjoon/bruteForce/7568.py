n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split(' '))))
result=[0 for i in range(n)]
for i in range(n):
    count=0
    for j in arr:
        if arr[i][0]<j[0] and arr[i][1]<j[1]:
            count+=1
    result[i]=count+1
result=list(map(str,result))
print(" ".join(result))