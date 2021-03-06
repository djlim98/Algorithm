from collections import deque
def bfs(i,j):
    dq=deque()
    dq.append([i,j])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while dq:
        i,j=dq.popleft()
        for k in range(4):
            x=i+dx[k]
            y=j+dy[k]
            if 0 <= x < n and 0 <= y < m and Map[x][y] == 1:
                Map[x][y] = 0
                dq.append([x, y])
t=int(input())
for p in range(t):
    m,n,baechu=list(map(int,input().split(' ')))
    Map=[[0 for i in range(m)] for j in range(n)]
    bSet=0
    for i in range(baechu):
        y,x=list(map(int,input().split(' ')))
        Map[x][y]=1
    for i in range(n):
        for j in range(m):
            if Map[i][j]==1:
                bfs(i,j)
                bSet+=1
    print(bSet)
