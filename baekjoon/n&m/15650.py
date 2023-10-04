n, m = map(int, input().split(" "))

s = []


def check_small(d, f):
    for i in d:
        if i > f:
            return False
    return True


def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return

    for i in range(1, n + 1):
        if i not in s and check_small(s, i):
            s.append(i)
            dfs()
            s.pop()


dfs()
