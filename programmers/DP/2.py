#https://programmers.co.kr/learn/courses/30/lessons/43105
def solution(triangle):
    answer = 0
    if len(triangle)==1:
        return triangle[0][0]
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j==0:
                triangle[i][j]+=triangle[i-1][0]
            elif j==len(triangle[i])-1:
                triangle[i][j]+=triangle[i-1][-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
    answer=max(triangle[-1])
    return answer
