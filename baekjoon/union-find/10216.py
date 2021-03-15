import math
T=int(input())
for t in range(T):

    n=int(input())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split(' '))))
    network=[i for i in range(n)]
    
    def isMeet(a,b):
        return math.sqrt((arr[a][0]-arr[b][0])**2+(arr[a][1]-arr[b][1])**2)<=(arr[a][2]+arr[b][2])
    
    for i in range(n):
        for j in range(i,n):
            if isMeet(i,j):
                king=min(network[i],network[j])
                network[i]=king
                network[j]=king
    for i in range(n):
        stack=[]
        while stack:
            
    print(len(set(network)))