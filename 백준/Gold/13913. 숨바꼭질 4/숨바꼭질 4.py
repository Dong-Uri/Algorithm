from collections import deque

N, K = map(int, input().split())
que = deque()
que.append((N, 0))
visited = [-1] * 100001
visited[N] = -2
while que:
    n, cnt = que.popleft()
    if n == K:
        break
    cnt += 1
    if n != 0 and visited[n-1] == -1:
        visited[n-1] = n
        que.append((n-1, cnt))
    if n != 100000 and visited[n+1] == -1:
        visited[n+1] = n
        que.append((n+1, cnt))
    if 2 <= n <= 50000 and visited[n*2] == -1:
        visited[n*2] = n
        que.append((n*2, cnt))
print(cnt)
ans = [K]
while True:
    K = visited[K]
    if K == -2:
        break
    ans.append(K)
print(*ans[::-1])