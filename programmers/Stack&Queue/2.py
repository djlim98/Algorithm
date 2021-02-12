def solution(progresses, speeds):
    answer = []
    while(progresses):
        progresses=list(map(lambda x :x[1]+speeds[x[0]], tuple(enumerate(progresses))))
        count=0
        while(progresses[0]>=100):
            del progresses[0]
            del speeds[0]
            count+=1
            if not progresses:
                break
        if count>0:
            answer.append(count)

    return answer
    #https://programmers.co.kr/learn/courses/30/lessons/42586
