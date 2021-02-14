#https://programmers.co.kr/learn/courses/30/lessons/42628
import heapq as hq

def solution(operations):
    answer = []
    maxheap=[]
    minheap=[]
    for i in operations:
        inputarr=i.split(' ')
        code=inputarr[0]
        value=int(inputarr[1])
        
        if code=='I':
            hq.heappush(minheap, value)
            hq.heappush(maxheap,(-value,value))
        elif code=='D':
            if not minheap:
                continue
            if value==-1:
                deleteV=hq.heappop(minheap)
                maxheap.remove((-deleteV,deleteV))
            elif value==1:
                deleteV=hq.heappop(maxheap)[1]
                minheap.remove(deleteV)
    if minheap:
        minV=hq.heappop(minheap)
        maxV=hq.heappop(maxheap)[1]
        answer=[maxV,minV]
    else:
        answer=[0,0]
    return answer
