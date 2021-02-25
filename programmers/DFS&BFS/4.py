from collections import deque

def solution2(tickets):
    answer = []
    tickets.sort(key=lambda x:x[1])

    road=deque()
    start='ICN'

    road.append(start)

    while tickets:
        for i in tickets:
            if i[0]==start:
                road.append(i[1])
                start=i[1]
                tickets.remove(i)
                break        
            elif i==tickets[-1]:
                end=road[0]
                tickets.sort(key=lambda x:x[0],reverse=True)

                while tickets:
                    for j in tickets:
                        if j[1]==end:
                            road.appendleft(j[0])
                            end=j[0]
                            tickets.remove(j)
                            break

    answer=list(road)
    return answer

def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    
    st = ['ICN']
    ans = []
    while st:
        top = st[-1]
        if top not in routes or len(routes[top])==0:
            ans.append(st.pop())
        else:
            st.append(routes[top].pop())
    ans.reverse()
    return ans
