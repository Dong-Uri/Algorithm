N, M = map(int, input().split())
war = []
for _ in range(M):
    war.append(input())
W = 0
B = 0
ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False] * N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        stack = [[i, j]]
        visited[i][j] = True
        power = 1
        while stack:
            now = stack.pop()
            for w in ways:
                new = [now[0] + w[0], now[1] + w[1]]
                if new[0] < 0 or new[0] >= M:
                    continue
                if new[1] < 0 or new[1] >= N:
                    continue
                if war[new[0]][new[1]] != war[i][j]:
                    continue
                if visited[new[0]][new[1]]:
                    continue
                power += 1
                stack.append(new)
                visited[new[0]][new[1]] = True
        if war[i][j] == 'W':
            W += power ** 2
        else:
            B += power ** 2
print(W, B)