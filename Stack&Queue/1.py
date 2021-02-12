def solution(prices):
    answer = [0 for i in range(len(prices))]
    stack=[]
    for i in range(len(prices)):
        if not stack:
            stack.append(i)
            continue
        while(prices[stack[-1]]>prices[i]):
            popPoint=stack.pop()
            answer[popPoint]=i-popPoint
            if not stack:
                break
        stack.append(i)
    while(stack):
        popPoint=stack.pop()
        answer[popPoint]=len(prices)-popPoint-1
        
            
    return answer
    #https://programmers.co.kr/learn/courses/30/lessons/42584
