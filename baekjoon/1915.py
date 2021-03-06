size=list(map(int,input().split(' ')))
array=[[0 for i in range(size[1]+1)]]
for i in range(size[0]):
    array.append([0]+list(map(int,list(input().strip()))))

max_square=0

for i in range(1, size[0]+1):
    for j in range(1, size[1]+1):
        if array[i][j]==1:
            array[i][j]=min(array[i-1][j],array[i-1][j-1],array[i][j-1])+1
        max_square=max(max_square,array[i][j])

print(max_square**2)


