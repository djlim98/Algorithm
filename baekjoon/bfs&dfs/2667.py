from collections import deque
def bfs(i,j):
    dq=deque()
    dq.append([i,j])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    count=1
    while dq:
        i,j=dq.popleft()
        for k in range(4):
            x=i+dx[k]
            y=j+dy[k]
            if 0 <= x < n and 0 <= y < n and Hmap[x][y] == 1:
                Hmap[x][y] = 0
                dq.append([x, y])
                count += 1
    setArr.append(count)

n=int(input())
Hmap=[]
for i in range(n):
    Hmap.append(list(map(int,list(input().strip()))))
setArr=[]
for i in range(n):
    for j in range(n):
        if Hmap[i][j]==1:
            Hmap[i][j]=0
            bfs(i,j)
setArr.sort()
print(len(setArr))
for i in setArr:
    print(i)