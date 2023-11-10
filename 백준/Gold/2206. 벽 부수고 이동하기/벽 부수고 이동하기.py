import sys
from collections import deque
import copy
N, M = map(int, sys.stdin.readline().rstrip().split())
map_unbroken = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
map_broken = copy.deepcopy(map_unbroken)
que = deque()
que.append([0, 0, 1]) # i, j, 벽을 부쉈는지
map_unbroken[0][0] = 2
map_broken[0][0] = 2
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
while que and map_unbroken[N-1][M-1] == 0 and map_broken[N-1][M-1] == 0:
    now = que.popleft()
    for n in range(4):
        ni = now[0] + di[n]
        nj = now[1] + dj[n]
        if 0 <= ni < N and 0 <= nj < M:
            if now[2]:
                if map_unbroken[ni][nj] == 0:
                    map_broken[ni][nj] = map_unbroken[ni][nj] = map_unbroken[now[0]][now[1]] + 1
                    que.append([ni, nj, 1])
                elif map_unbroken[ni][nj] == 1:
                    map_broken[ni][nj] = map_unbroken[ni][nj] = map_unbroken[now[0]][now[1]] + 1
                    que.append([ni, nj, 0])
            elif map_broken[ni][nj] == 0:
                map_broken[ni][nj] = map_broken[now[0]][now[1]] + 1
                que.append([ni, nj, 0])
print(max(map_unbroken[N-1][M-1], map_broken[N-1][M-1]) - 1)