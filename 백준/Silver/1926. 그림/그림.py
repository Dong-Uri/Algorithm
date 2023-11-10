n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))
answer = [0, 0]
ways = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    for j in range(m):
        if not paper[i][j]:
            continue
        answer[0] += 1
        cnt = 0
        paper[i][j] = 0
        stack = [[i, j]]
        while stack:
            cnt += 1
            now = stack.pop()
            for w in ways:
                new = [now[0] + w[0], now[1] + w[1]]
                if new[0] < 0 or new[0] >= n:
                    continue
                if new[1] < 0 or new[1] >= m:
                    continue
                if paper[new[0]][new[1]] == 0:
                    continue
                paper[new[0]][new[1]] = 0
                stack.append(new)
        if cnt > answer[1]:
            answer[1] = cnt
print(answer[0])
print(answer[1])