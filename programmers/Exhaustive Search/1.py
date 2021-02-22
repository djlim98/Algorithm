#https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    c1,c2,c3=[0,0,0]
    a=list(enumerate(answers))
    
    def check_answer(answer):
        nonlocal c1,c2,c3
        c2_rule={1:1, 3:3, 5:4, 7:5,0:0,2:0,4:0,6:0}
        c3_rule={0:3,1:3,2:1,3:1,4:2,5:2,6:4,7:4,8:5,9:5}
        
        if answer[0]%5+1==answer[1]:
            c1+=1
        if (answer[0]%2==0 and answer[1]==2) or (c2_rule[answer[0]%8]==answer[1]):
            c2+=1
        if c3_rule[answer[0]%10]==answer[1]:
            c3+=1
    
    list(map(check_answer,a))
    answerman=max(c1,c2,c3)
    for i in enumerate([c1,c2,c3]):
        if answerman==i[1]:
            answer.append(i[0]+1)
    return answer
