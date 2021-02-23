#https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    result=[number[0]]
    i=0
    for i in number[1:]:
        while len(result)>0and result[-1]<i  and k>0:
            result.pop()
            k-=1
        result.append(i)            
    if k!=0:
        result=result[:-k]
    answer=''.join(result)
    return answer
    
