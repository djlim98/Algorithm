#https://programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    people=deque(people)
    while people:
        if people[0]<=limit/2:
            answer+=int((len(people)+1)/2)
            break
        if len(people)>1 and people[0]+people[-1]<=limit:
            people.pop()
            people.popleft()
        else:
            people.popleft()
        answer+=1
    return answer
