from collections import deque

N, K = map(int, input().split())
que = deque()
que.append((N, 0))
visited = [[-1, 0] for _ in range(100001)]
visited[N][0] = 0
visited[N][1] = 1
while que:
    n, cnt = que.popleft()
    if visited[K][0] != -1 and cnt > visited[K][0]:
        break
    cnt += 1
    if n != 0:
        if visited[n - 1][0] == -1:
            visited[n - 1][0] = cnt
            visited[n - 1][1] += visited[n][1]
            que.append((n - 1, cnt))
        elif visited[n - 1][0] == cnt:
            visited[n - 1][1] += visited[n][1]
    if n != 100000:
        if visited[n + 1][0] == -1:
            visited[n + 1][0] = cnt
            visited[n + 1][1] += visited[n][1]
            que.append((n + 1, cnt))
        elif visited[n + 1][0] == cnt:
            visited[n + 1][1] += visited[n][1]
    if n*2 <= 100000:
        if visited[n * 2][0] == -1:
            visited[n * 2][0] = cnt
            visited[n * 2][1] += visited[n][1]
            que.append((n * 2, cnt))
        elif visited[n * 2][0] == cnt:
            visited[n * 2][1] += visited[n][1]
print(visited[K][0])
print(visited[K][1])
