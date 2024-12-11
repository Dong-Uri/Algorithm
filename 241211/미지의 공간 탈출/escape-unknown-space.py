from collections import deque

N, M, F = map(int, input().split())

spaces = [[] for _ in range(6)]
for _ in range(N):
    spaces[0].append(list(map(int, input().split())))
for i in range(5):
    for _ in range(M):
        spaces[i + 1].append(list(map(int, input().split())))

phenomena = []
for _ in range(F):
    r, c, d, v = map(int, input().split())
    phenomena.append([r, c, d, v, v])

for i in range(N):
    for j in range(N):
        if spaces[0][i][j] == 3:
            break
    if spaces[0][i][j] == 3:
        break
tws = [i, j]

for i in range(M):
    for j in range(M):
        if spaces[5][i][j] == 2:
            break
    if spaces[5][i][j] == 2:
        break
TM = deque([[5, i, j, 0]])

for r, c, _, _, _ in phenomena:
    spaces[0][r][c] = 1

ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
answer = -1
while TM and answer == -1:
    
    new_phenomena = []
    for r, c, d, v, cnt in phenomena:
        cnt -= 1
        if cnt == 0:
            r += ways[d][0]
            c += ways[d][1]
            if spaces[0][r][c]:
                continue
            spaces[0][r][c] = 1
            cnt = v
        new_phenomena.append([r, c, d, v, cnt])
    phenomena = new_phenomena

    now = TM.popleft()
    for wi, wj in ways:
        nxt = [now[0], now[1] + wi, now[2] + wj, now[3] + 1]
        if nxt[0] == 0:
            if nxt[1] == -1 or nxt[1] == N or nxt[2] == -1 or nxt[2] == N:
                continue
            if spaces[nxt[0]][nxt[1]][nxt[2]] == 4:
                answer = nxt[3]
            if spaces[nxt[0]][nxt[1]][nxt[2]] == 0:
                spaces[nxt[0]][nxt[1]][nxt[2]] = 1
                TM.append(nxt)
        if nxt[0] == 1:
            if nxt[1] == -1:
                nxt[0] = 5
                nxt[1] = M - 1 - nxt[2]
                nxt[2] = M - 1
            elif nxt[1] == M:
                nxt[0] = 0
                nxt[1] = tws[0] + M - 1 - nxt[2]
                nxt[2] = tws[1] + M
            elif nxt[2] == -1:
                nxt[0] = 3
                nxt[2] = M - 1
            elif nxt[2] == M:
                nxt[0] = 4
                nxt[2] = 0
            if spaces[nxt[0]][nxt[1]][nxt[2]] == 0:
                spaces[nxt[0]][nxt[1]][nxt[2]] = 1
                TM.append(nxt)
        if nxt[0] == 2:
            if nxt[1] == -1:
                nxt[0] = 5
                nxt[1] = nxt[2]
                nxt[2] = 0
            elif nxt[1] == M:
                nxt[0] = 0
                nxt[1] = tws[0] + nxt[2]
                nxt[2] = tws[1] - 1
            elif nxt[2] == -1:
                nxt[0] = 4
                nxt[2] = M - 1
            elif nxt[2] == M:
                nxt[0] = 3
                nxt[2] = 0
            if spaces[nxt[0]][nxt[1]][nxt[2]] == 0:
                spaces[nxt[0]][nxt[1]][nxt[2]] = 1
                TM.append(nxt)
        if nxt[0] == 3:
            if nxt[1] == -1:
                nxt[0] = 5
                nxt[1] = M - 1
            elif nxt[1] == M:
                nxt[0] = 0
                nxt[1] = tws[0] + M
                nxt[2] = tws[1] + nxt[2]
            elif nxt[2] == -1:
                nxt[0] = 2
                nxt[2] = M - 1
            elif nxt[2] == M:
                nxt[0] = 1
                nxt[2] = 0
            if spaces[nxt[0]][nxt[1]][nxt[2]] == 0:
                spaces[nxt[0]][nxt[1]][nxt[2]] = 1
                TM.append(nxt)
        if nxt[0] == 4:
            if nxt[1] == -1:
                nxt[0] = 5
                nxt[1] = 0
                nxt[2] = M - 1 - nxt[2]
            elif nxt[1] == M:
                nxt[0] = 0
                nxt[1] = tws[0] - 1
                nxt[2] = tws[1] + M - 1 - nxt[2]
            elif nxt[2] == -1:
                nxt[0] = 1
                nxt[2] = M - 1
            elif nxt[2] == M:
                nxt[0] = 2
                nxt[2] = 0
            if spaces[nxt[0]][nxt[1]][nxt[2]] == 0:
                spaces[nxt[0]][nxt[1]][nxt[2]] = 1
                TM.append(nxt)
        if nxt[0] == 5:
            if nxt[1] == -1:
                nxt[0] = 4
                nxt[1] = 0
                nxt[2] = M - 1 - nxt[2]
            elif nxt[1] == M:
                nxt[0] = 3
                nxt[1] = 0
            elif nxt[2] == -1:
                nxt[0] = 2
                nxt[2] = nxt[1]
                nxt[1] = 0
            elif nxt[2] == M:
                nxt[0] = 1
                nxt[2] = M - 1 - nxt[1]
                nxt[1] = 0
            if spaces[nxt[0]][nxt[1]][nxt[2]] == 0:
                spaces[nxt[0]][nxt[1]][nxt[2]] = 1
                TM.append(nxt)

print(answer)