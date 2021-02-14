#https://programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):
    answer = 0
    count=0
    while priorities:
        candinate=priorities.pop(0)
        location-=1
        flag=True
        for i in priorities:
            if candinate<i:
                flag=False
                break
        if not flag:
            priorities.append(candinate)
            if location==-1:
                location+=len(priorities)
        else:
            count+=1
            if location==-1:
                answer=count
                break
        
    return answer
