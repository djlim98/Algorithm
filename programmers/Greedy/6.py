#https://programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    answer = 0
    car=list(map(lambda x:(x[1],x[0]),routes))
    car.sort()
    mint=-30001
    for i in car:
        if i[1]>mint:
            answer+=1
            mint=i[0]
    return answer
