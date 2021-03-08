from collections import deque

n,m=list(map(int,input().split(' ')))
baguni=[]
for i in range(m):
    baguni.append(list(map(int,input().strip().split(' '))))
dq=deque()

for i in range(m):
    for j in range(n):
        if baguni[i][j]==1:
            dq.append([i,j])
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
while dq:
    i,j=dq.popleft()
    for k in range(4):
        x=i+dx[k]
        y=j+dy[k]
        if 0 <= x < m and 0 <= y < n and baguni[x][y] == 0:
            dq.append([x,y])
            baguni[x][y] = baguni[i][j]+1

flag=False
result=-2

for i in range(m):
    for j in range(n):
        if baguni[i][j]==0:
            flag=True
        result=max(result,baguni[i][j])
if flag:
    print(-1)
elif result==-1:
    print(0)
else:
    print(result-1)