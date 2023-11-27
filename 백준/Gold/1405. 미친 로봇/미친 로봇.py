def move(x, y, n, stat, vst):
    global ans
    if n == N:
        per = 1
        per *= (X / 100) ** stat[0]
        per *= (Y / 100) ** stat[1]
        per *= (Z / 100) ** stat[2]
        per *= (W / 100) ** stat[3]
        ans += per
        # print(ans)
        return
    for i in range(4):
        x += ways[i][0]
        y += ways[i][1]
        stat[i] += 1
        if not vst[x][y]:
            vst[x][y] = True
            move(x, y, n + 1, stat, vst)
            vst[x][y] = False
        stat[i] -= 1
        x -= ways[i][0]
        y -= ways[i][1]

N, X, Y, Z, W = map(int, input().split())
ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = [[False for _ in range(30)] for _ in range(30)]
visited[0][0] = True
ans = 0
move(0, 0, 0, [0, 0, 0, 0], visited)
print(ans)