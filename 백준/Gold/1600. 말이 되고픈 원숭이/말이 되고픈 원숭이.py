from collections import deque
import sys

K = int(sys.stdin.readline().rstrip())
W, H = map(int, sys.stdin.readline().rstrip().split())
grid = []
for _ in range(H):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    grid.append(line)
inf = W * H
visited = [[[inf] * (K + 1) for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if grid[i][j]:
            visited[i][j] = False
visited[0][0] = [0] * (K + 1)
monkey = [(1, 0), (-1, 0), (0, 1), (0, -1)]
horse = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
deq = deque([[0, 0, 0]])
while deq and visited[H - 1][W - 1][K] == inf:
    x, y, n = deq.popleft()
    mov = visited[x][y][n] + 1
    for m in monkey:
        nx = x + m[0]
        ny = y + m[1]
        if nx >= 0 and nx < H and ny >= 0 and ny < W and visited[nx][ny]:
            if visited[nx][ny][n] > mov:
                visited[nx][ny][n] = mov
                deq.append([nx, ny, n])
                nn = n + 1
                while nn <= K and visited[nx][ny][nn] > mov:
                    visited[nx][ny][nn] = mov
                    nn += 1
    if n != K:
        for h in horse:
            nx = x + h[0]
            ny = y + h[1]
            if nx >= 0 and nx < H and ny >= 0 and ny < W and visited[nx][ny]:
                if visited[nx][ny][n + 1] > mov:
                    visited[nx][ny][n + 1] = mov
                    deq.append([nx, ny, n + 1])
                    nn = n + 2
                    while nn <= K and visited[nx][ny][nn] > mov:
                        visited[nx][ny][nn] = mov
                        nn += 1
answer = visited[H - 1][W - 1][K]
if answer == inf:
    answer = -1
print(answer)