#https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    find=sorted(lost)
    for i in find:
        if reserve.count(i) :
            reserve.remove(i)
            lost.remove(i)
    find=sorted(lost)
    for i in find:
        if i-1 in reserve:
            lost.remove(i)
            reserve.remove(i-1)
        elif i+1 in reserve:
            lost.remove(i)
            reserve.remove(i+1)

    answer=n-len(lost)
    return answer
