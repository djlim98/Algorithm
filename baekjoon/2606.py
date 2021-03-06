from collections import deque
n=int(input())
m=int(input())
E=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(m):
    x,y=list(map(int,input().split(' ')))
    E[x][y]=1
    E[y][x]=1

visit=[0 for i in range(n+1)]
dq=deque()
dq.append(1)
visit[1]=1
while True:
    node=dq.popleft()
    for i in range(1,n+1):
        if E[node][i]==1 and visit[i]==0:
            visit[i]=1
            dq.append(i)
    if len(dq)==0:
        break
print(visit.count(1)-1)