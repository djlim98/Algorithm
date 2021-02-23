#https://programmers.co.kr/learn/courses/30/lessons/42861
def solution(n, costs):
    answer = 0
    island=[i for i in range(1,n)]
    connected=[0]
    while len(connected)<n:
        road=[]
        for i in costs:
            if i[0] in connected:
                if i[1] not in connected:
                    road.append((i[2],i[1]))
            elif i[1] in connected:
                if i[0] not in connected:
                    road.append((i[2],i[0]))
        cr=min(road)
        answer+=cr[0]
        connected.append(cr[1])
    return answer
