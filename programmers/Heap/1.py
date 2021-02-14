#https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0]<K:
        if len(scoville)==1:
            answer=-1
            break
        f1=heapq.heappop(scoville)
        f2=heapq.heappop(scoville)
        
        new=f1+f2*2
        heapq.heappush(scoville,new)        
        answer+=1
    return answer
