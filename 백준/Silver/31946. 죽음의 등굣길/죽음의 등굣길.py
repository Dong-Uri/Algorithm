import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
blocks = []
for _ in range(N):
    blocks.append(list(map(int, input().split())))
X = int(input())
b = blocks[0][0]
if blocks[-1][-1] != b:
    print('DEAD')
else:
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    stack = [[0, 0]]
    while stack:
        n, m = stack.pop()
        for i in range(N):
            for j in range(M):
                if not visited[i][j]:
                    if abs(n - i) + abs(m - j) <= X:
                        visited[i][j] = True
                        if blocks[i][j] == b:
                            stack.append([i, j])
    if visited[-1][-1]:
        print('ALIVE')
    else:
        print('DEAD')