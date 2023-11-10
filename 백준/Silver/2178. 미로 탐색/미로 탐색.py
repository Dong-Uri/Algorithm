N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(input())
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
queue = [[0,0]]
while visited[N-1][M-1] == 0:
    now = queue.pop(0)
    move = [[now[0],now[1]-1], [now[0],now[1]+1], [now[0]+1,now[1]], [now[0]-1,now[1]]]
    for m in move:
        if 0 <= m[0] < N and 0 <= m[1] < M and maze[m[0]][m[1]] == '1' and visited[m[0]][m[1]] == 0:
            visited[m[0]][m[1]] = visited[now[0]][now[1]] + 1
            queue.append(m)
print(visited[N-1][M-1])