from collections import deque
N, K = map(int, input().split())
place = [-1] * 100001
que = deque()
que.append(K)
place[K] = 0
n = 0
while True:
    now = que.popleft()
    if now == N:
        break
    if now % 2 == 0 and (place[now // 2] == -1 or place[now // 2] > place[now]):
        place[now // 2] = place[now]
        que.appendleft(now // 2)
    if now - 1 >= 0 and (place[now - 1] == -1 or place[now - 1] > place[now] + 1):
        place[now - 1] = place[now] + 1
        que.append(now - 1)
    if now + 1 <= 100000 and (place[now + 1] == -1 or place[now + 1] > place[now] + 1):
        place[now + 1] = place[now] + 1
        que.append(now + 1)
print(place[N])