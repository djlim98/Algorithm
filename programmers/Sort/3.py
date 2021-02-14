def solution(citations):
    answer = 0
    citations.sort()
    n=len(citations)
    #print(citations)
    while True:
        idx=n-1
        count=len(list(filter(lambda x:x>=n,citations)))
        #print(count, citations[idx],n)
        if count>=n and citations[idx]>=n:
            answer=n
            break
        n-=1
        
    return answer
    #https://programmers.co.kr/learn/courses/30/lessons/42747
