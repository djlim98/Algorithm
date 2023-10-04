n, m = map(int, input().split())

s = list(map(int, input().split()))
s = sorted(s)
result = []


def dfs():
    if len(result) == m:
        print(" ".join(map(str, result)))
        return

    for i in range(0, n):
        result.append(s[i])
        dfs()
        result.pop()


dfs()
