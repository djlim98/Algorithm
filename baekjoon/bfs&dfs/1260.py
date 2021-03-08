from collections import deque
def dfs(node):
    visit[node]=1
    for i in range(n):
        if E[node][i]==1 and visit[i]==0:
            print(i+1,end=' ')
            dfs(i)

def bfs(node):
    visit[node]=1
    dq=deque()

    while True:
        for i in range(n):
            if E[node][i]==1 and visit[i]==0:
                print(i+1, end=' ')
                visit[i]=1
                dq.append(i)
        if len(dq)==0:
            break
        node=dq.popleft()
        


n, e, s=list(map(int,input().split(' ')))
E=[[0 for i in range(n)] for j in range(n)]
visit=[0 for j in range(n)]
for i in range(e):
    x,y=list(map(int,input().split(' ')))
    E[x-1][y-1]=1
    E[y-1][x-1]=1

print(s,end=' ')
dfs(s-1)
print()
visit=[0 for j in range(n)]
print(s,end=' ')
bfs(s-1)