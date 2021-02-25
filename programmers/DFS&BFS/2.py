def solution(n, computers):
    answer = 0
    not_v=[i for i in range(n)]
    stack=[]
    
    while not_v:
        v=not_v.pop()
        stack.append(v)
        while stack:
            v=stack.pop()
            for i in range(len(computers[v])):
                if computers[v][i]==1:
                    if i in not_v:
                        not_v.remove(i)
                        stack.append(i)
        answer+=1
        
    return answer
