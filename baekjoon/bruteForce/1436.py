n=int(input())
number=666
count=1
while count<n:
    number+=1
    digit=str(number)
    if '666' in digit:
        count+=1
print(number)