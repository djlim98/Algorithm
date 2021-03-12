n=int(input())
digit=len(str(n))
start=n-digit*9
if start<0:
    start=0
result=0
while start<=n:
    if n==start+sum(list(map(int,list(str(start))))):
        result=start
        break
    start+=1
print(result)