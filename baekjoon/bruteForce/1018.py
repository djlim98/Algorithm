n,k=map(int,input().split(' '))
arr=[]
for i in range(n):
    arr.append(list(input()))

b_arr=[[0 for i in range(k)] for j in range(n)]
w_arr=[[0 for i in range(k)] for j in range(n)]

for i in range(n):
    for j in range(k):
        if (i+j)%2==0:
            if arr[i][j]=='W':
                w_arr[i][j]=0
                b_arr[i][j]=1
            else:
                w_arr[i][j]=1
                b_arr[i][j]=0
        else:
            if arr[i][j]=='W':
                w_arr[i][j]=1
                b_arr[i][j]=0
            else:
                w_arr[i][j]=0
                b_arr[i][j]=1
result=[]
for i in range(n-7):
    for j in range(k-7):
        temp=0
        mini=w_arr[i:i+8]
        for a in mini:
            mini_y=a[j:j+8]
            temp+=sum(mini_y)
        result.append(temp)
        
        temp=0
        mini=b_arr[i:i+8]
        for a in mini:
            mini_y=a[j:j+8]
            temp+=sum(mini_y)
        result.append(temp)
print(min(result))
