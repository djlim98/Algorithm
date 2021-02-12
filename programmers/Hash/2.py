def solution(phone_book):
    answer = True
    phone_book=sorted(phone_book)
    for i in range(len(phone_book)-1):
        result=phone_book[i+1].find(phone_book[i])
        print(result,phone_book[i],phone_book[i+1])
        if result==-1:
            continue
        elif result==0:
            answer=False
            break

    return answer
    
    #https://programmers.co.kr/learn/courses/30/lessons/42577
