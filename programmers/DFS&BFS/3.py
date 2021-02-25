def vailed(text,words):
    result=[]
    for word in words:
        count=0
        for i in range(len(text)):
            if text[i]!=word[i]:
                count+=1
        if count<=1:
            result.append(word)
    return result

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return answer
    
    stack=[begin]
    while words:
        next_stack=[]
        for i in stack:
            next_stack+=vailed(i,words)
        stack=list(set(next_stack))
        for v in stack:
            words.remove(v)
        answer+=1
        if target in stack:
            return answer

    return answer
