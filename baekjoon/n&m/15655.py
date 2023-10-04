n, m = map(int, input().split())

s = list(map(int, input().split()))
s = sorted(s)
result = []


def dfs(start):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return

    for i in range(start, n):
        if s[i] not in result:
            result.append(s[i])
            dfs(i + 1)
            result.pop()


dfs(0)
