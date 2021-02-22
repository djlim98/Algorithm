#https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def check_prime(candidate):
    temp=0
    candidate=set(list(map(int,candidate)))
    candidate=list(candidate)
    for num in candidate:
        prime=True
        if num==1 or num==0:
            continue
        for i in range(num):
            if (i+1)==1 or (i+1)==num:
                continue
            if num%(i+1)==0:
                prime=False
                break
        if prime:
            temp+=1
            
    return temp

def solution(numbers):
    num_set=[]
    for digit in range(len(numbers)):
        candidate=list(map(''.join, permutations(numbers,digit+1)))
        num_set+=candidate
    answer=check_prime(num_set)
    return answer
