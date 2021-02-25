def solution(m, n, puddles):
    answer = 0
    a=[[1 if i==0 and j==0 else 0  for i in range(m)]for j in range(n)]

    for i in puddles:
        a[i[1]-1][i[0]-1]=-1
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j]==-1:
                continue
            if i==0 and j==0:
                continue
            if i-1<0 or a[i-1][j]==-1:
                a[i][j]+=a[i][j-1]
            elif j-1<0 or a[i][j-1]==-1:
                a[i][j]+=a[i-1][j]
            else:
                a[i][j]+=a[i-1][j]+a[i][j-1]
    answer=a[-1][-1]%1000000007
    return answer
