#https://programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    answer = 0
    name=list(name)
    
    for i in name:
        time=min(ord(i)-65,91-ord(i))
        answer+=time
    
    jump=0
    i=0
    while name!=list('A'*len(name)):
        if name[i]!='A':
            name[i]='A'
        
        goal=[]
        
        for index in range(len(name)):
            if name[index]!='A':
                goal.append(index)
        
        if len(goal)==0:
            break
        
        goal_info=list(map(lambda x:(min(abs(x-i),len(name)-x+i),x),goal))
        min_goal=min(goal_info)

        i=min_goal[1]
        jump+=min_goal[0]
        
    return answer+jump
