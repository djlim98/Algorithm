from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')

#이진탐색
# from sys import stdin, stdout
# n = stdin.readline()
# N = sorted(map(int,stdin.readline().split()))
# m = stdin.readline()
# M = map(int, stdin.readline().split())

# def binary(l, N, start, end):
#     if start > end:
#         return 0
#     m = (start+end)//2
#     if l == N[m]:
#         return 1
#     elif l < N[m]:
#         return binary(l, N, start, m-1)
#     else:
#         return binary(l, N, m+1, end)

# for l in M:
#     start = 0
#     end = len(N)-1
#     print(binary(l,N,start,end))