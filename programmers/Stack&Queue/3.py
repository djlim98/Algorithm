def solution(bridge_length, weight, truck_weights):
    answer = 1
    currentT=[]
    time=[0]*len(truck_weights)
    while(truck_weights or currentT):
        #print(truck_weights)
        #print(currentT)
        #print(time)
        if truck_weights and weight>=sum(currentT)+truck_weights[0]:
            currentT.append(truck_weights.pop(0))
        for i in range(len(currentT)):
            time[i]+=1
        result=[]
        for i in time:
            if i!=bridge_length:
                result.append(i)
            else:
                currentT.pop(0)
        time=result        
        answer+=1
        
        
    return answer
    #https://programmers.co.kr/learn/courses/30/lessons/42583
