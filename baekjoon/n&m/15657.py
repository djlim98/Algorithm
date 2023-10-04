n, m = map(int, input().split())

s = sorted(list(map(int, input().split())))

result = []

visit = [False for i in range(n)]


def dfs():
    if len(result) == m:
        temp = " ".join(map(str, result))

        print(temp)

        return
    remember = 0
    for i in range(0, n):
        if not visit[i] and remember != s[i]:
            result.append(s[i])
            remember = s[i]
            visit[i] = True
            dfs()
            visit[i] = False
            result.pop()


dfs()
