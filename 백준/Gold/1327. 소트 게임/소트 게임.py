from collections import deque

N, K = map(int, input().split())
start = list(map(int, input().split()))
visited = set()
visited.add(str(start))
end = [n + 1 for n in range(N)]
if start == end:
    ans = 0
    now = False
else:
    now = deque([[start, 0]])
    ans = -1
while now:
    n, att = now.popleft()
    for x in range(N - K + 1):
        new_n = n[:]
        base = 2 * x + K - 1
        for i in range(x, x + K):
            new_n[i] = n[base - i]
        if str(new_n) in visited:
            continue
        if new_n == end:
            ans = att + 1
            break
        visited.add(str(new_n))
        now.append([new_n, att + 1])
    if new_n == end:
        break
print(ans)