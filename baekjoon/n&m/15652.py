n, m = map(int, input().split(" "))

s = []


def dfs(start):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(start, 1 + n):
        s.append(i)
        dfs(i)
        s.pop()


dfs(1)
