#https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    total=brown+yellow
    for x in range(1,total+1):
        if total%x!=0:
            continue
        y=total/x
        if (x-2)*(y-2)==yellow:
            answer=[y,x]
            break
    return answer
