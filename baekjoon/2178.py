from collections import deque

n,m=list(map(int,input().split(' ')))
miro=[]
for i in range(n):
    miro.append(list(map(int,list(input().strip()))))

dq=deque()
dq.append([0,0])
miro[0][0]=0
while dq:
    i,j=dq.popleft()
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    for p in range(4):
        x=i+dx[p]
        y=j+dy[p]
        if 0<=x<n and 0<=y<m and miro[x][y]>0:
            miro[x][y]=miro[i][j]-1
            if x==n-1 and y==m-1:
                print(-miro[x][y]+1)
                dq=[]
                break
            dq.append([x,y])
