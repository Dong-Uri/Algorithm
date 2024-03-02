N = int(input())
choco = []
for _ in range(N):
    line = input()
    choco.append(line)
connect = [[[] for _ in range(N)] for _ in range(N)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 0
for i in range(N):
    for j in range(N):
        if choco[i][j] == '#':
            cnt += 1
            for m in move:
                ni = i + m[0]
                nj = j + m[1]
                if ni >= 0 and ni < N and nj >= 0 and nj < N and choco[ni][nj] == '#':
                    connect[i][j].append([ni, nj])
answer = []
for i in range(N):
    for j in range(N):
        if choco[i][j] == '#':
            visited = [[False] * N for _ in range(N)]
            visited[i][j] = True
            now = connect[i][j][0]
            stack = [now]
            split_cnt = 1
            while stack:
                cycle = False
                new_stack = []
                for s in stack:
                    visited[s[0]][s[1]] = True
                    for c in connect[s[0]][s[1]]:
                        if not visited[c[0]][c[1]]:
                            if c in new_stack:
                                cycle = True
                                break
                            else:
                                new_stack.append(c)
                                split_cnt += 1
                if cycle:
                    break
                stack = new_stack
            else:
                if split_cnt == cnt - 1:
                    answer.append([i + 1, j + 1])
print(len(answer))
for a in answer:
    print(*a)
