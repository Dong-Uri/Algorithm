import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split())
way = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    way[A].append(B)
    way[B].append(A)
cnt[0].append(1)
visited[1] = True
que = deque()
que.append((1, 0))
while que:
    now, c = que.popleft()
    c += 1
    for n in way[now]:
        if not visited[n]:
            visited[n] = True
            que.append((n, c))
            cnt[c].append(n)
print(min(cnt[c-1]), c-1, len(cnt[c-1]))


