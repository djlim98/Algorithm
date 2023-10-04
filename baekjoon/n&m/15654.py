n, m = map(int, input().split())

s = list(map(int, input().split()))
s = sorted(s)
result = []


def dfs():
    if len(result) == m:
        print(" ".join(map(str, result)))
        return

    for i in s:
        if i not in result:
            result.append(i)
            dfs()
            result.pop()


dfs()
