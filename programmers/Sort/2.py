#https://programmers.co.kr/learn/courses/30/lessons/42746
from functools import cmp_to_key

def compare(x,y):
    if int(x+y)>=int(y+x):
        return 0
    else:
        return -1

def solution(num):
    str_list = [str(n) for n in num]
    answer=sorted(str_list, key=cmp_to_key(compare),reverse=True)
    answer=int(''.join(answer))
    return str(answer)
