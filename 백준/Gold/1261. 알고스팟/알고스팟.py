
import heapq

M, N = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
heap = []
heapq.heappush(heap, [0, 0, 0])
ways = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False] * M for _ in range(N)]
visited[0][0] = True
while True:
    now = heapq.heappop(heap)
    if now[1] == N-1 and now[2] == M-1:
        print(now[0])
        break
    for w in ways:
        new = [now[1] + w[0], now[2] + w[1]]
        if new[0] < 0 or new[0] >= N:
            continue
        if new[1] < 0 or new[1] >= M:
            continue
        if visited[new[0]][new[1]]:
            continue
        if miro[new[0]][new[1]]:
            heapq.heappush(heap, [now[0] + 1, new[0], new[1]])
        else:
            heapq.heappush(heap, [now[0], new[0], new[1]])
        visited[new[0]][new[1]] = True