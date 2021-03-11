from itertools import combinations

n, m = map(int,input().split(' '))
arr=list(map(int,input().split(' ')))

card=combinations(arr,3)
temp=-1
for i in card:
    a=sum(list(i))
    if temp<a<=m:
        temp=a

print(temp)