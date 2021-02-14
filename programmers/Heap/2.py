#https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq
def solution(jobs):
    answer = 0
    time=0
    total=0
    n=len(jobs)
    while jobs:
        current_work=list(filter(lambda i:i[0]<=time, jobs))
        if not current_work:
            time+=1
            continue
        current_work=list(map(lambda i: [i[1],i[0]], current_work))
        heapq.heapify(current_work)
        work=heapq.heappop(current_work)
        time+=work[0]
        answer+=time-work[1]
        jobs.remove([work[1],work[0]])
    answer=int(answer/n)
    return answer
