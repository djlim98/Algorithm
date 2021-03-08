from collections import deque

n,m=map(int,input().split(' '))
dq=deque()
dq.append(n)
visit=[0 for i in range(1000001)]
result=0
visit[n]=visit[n]+1
while dq:
    node=dq.popleft()
    dx=[node+1,node-1,node*2]
    for i in dx:
        if 0<=i<=100000 and visit[i]==0:
            dq.append(i)
            visit[i]=visit[node]+1
        elif m==i:
            result=visit[i]
            break
    if result!=0:
        break
print(result-1)

