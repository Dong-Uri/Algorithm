n, m = map(int, input().split())
ans = [[-1] * m for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] == 2:
            stack = [[i, j]]
            ans[i][j] = 0
        if line[j] == 0:
            ans[i][j] = 0
ways = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while stack:
    now = stack.pop(0)
    for w in ways:
        new = [now[0] + w[0], now[1] + w[1]]
        if new[0] < 0 or new[0] >= n:
            continue
        if new[1] < 0 or new[1] >= m:
            continue
        if ans[new[0]][new[1]] == -1:
            ans[new[0]][new[1]] = ans[now[0]][now[1]] + 1
            stack.append([new[0], new[1]])
        else:
            continue
for a in ans:
    print(*a)
