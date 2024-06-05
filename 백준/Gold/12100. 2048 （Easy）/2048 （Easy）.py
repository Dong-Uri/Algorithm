def move(n, bd, lst):
    global ans
    if n == 5:
        return
    bd_1 = [[0] * N for _ in range(N)]
    bd_2 = [[0] * N for _ in range(N)]
    bd_3 = [[0] * N for _ in range(N)]
    bd_4 = [[0] * N for _ in range(N)]
    for i in range(N):
        before = 0
        k = 0
        for j in range(N):
            if bd[i][j]:
                if before == bd[i][j]:
                    bd_1[i][k] = bd[i][j] * 2
                    if bd[i][j] == ans:
                        ans *= 2
                    before = 0
                    k += 1
                else:
                    if before:
                        bd_1[i][k] = before
                        k += 1
                    before = bd[i][j]
        if before:
            bd_1[i][k] = before
        before = 0
        k = N-1
        for j in range(N-1,-1,-1):
            if bd[i][j]:
                if before == bd[i][j]:
                    bd_2[i][k] = bd[i][j] * 2
                    if bd[i][j] == ans:
                        ans *= 2
                    before = 0
                    k -= 1
                else:
                    if before:
                        bd_2[i][k] = before
                        k -= 1
                    before = bd[i][j]
        if before:
            bd_2[i][k] = before
        before = 0
        k = 0
        for j in range(N):
            if bd[j][i]:
                if before == bd[j][i]:
                    bd_3[k][i] = bd[j][i] * 2
                    if bd[j][i] == ans:
                        ans *= 2
                    before = 0
                    k += 1
                else:
                    if before:
                        bd_3[k][i] = before
                        k += 1
                    before = bd[j][i]
        if before:
            bd_3[k][i] = before
        before = 0
        k = N-1
        for j in range(N-1,-1,-1):
            if bd[j][i]:
                if before == bd[j][i]:
                    bd_4[k][i] = bd[j][i] * 2
                    if bd[j][i] == ans:
                        ans *= 2
                    before = 0
                    k -= 1
                else:
                    if before:
                        bd_4[k][i] = before
                        k -= 1
                    before = bd[j][i]
        if before:
            bd_4[k][i] = before
    if bd != bd_1:
        move(n+1, bd_1, lst + ['left'])
    if bd != bd_2:
        move(n+1, bd_2, lst + ['right'])
    if bd != bd_3:
        move(n+1, bd_3, lst + ['up'])
    if bd != bd_4:
        move(n+1, bd_4, lst + ['down'])

N = int(input())
board = []
ans = 0
for _ in range(N):
    line = list(map(int, input().split()))
    if max(line) > ans:
        ans = max(line)
    board.append(line)
move(0, board, [])
print(ans)