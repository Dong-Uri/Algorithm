from collections import deque
N, K = map(int, input().split())
que = deque()
que.append(K)
cnt = [-1] * 100001
cnt[K] = 0
while True:
    num = que.popleft()
    if num % 2:
        next = [num + 1, num - 1]
    else:
        next = [num // 2, num + 1, num - 1]
    for n in next:
        if 0 <= n <= 100000 and cnt[n] == -1:
            que.append(n)
            cnt[n] = cnt[num] + 1
    if cnt[N] != -1:
        break
print(cnt[N])