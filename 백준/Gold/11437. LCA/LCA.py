import sys
input = sys.stdin.readline

N = int(input())
connect = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)
node_info = [[0, 0] for _ in range(N + 1)]
node_info[1][0] = 1
stack = [1]
while stack:
    node = stack.pop()
    for n in connect[node]:
        if not node_info[n][0]:
            node_info[n][0] = node_info[node][0] + 1
            node_info[n][1] = node
            stack.append(n)

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    while node_info[a][0] > node_info[b][0]:
        a = node_info[a][1]
    while node_info[a][0] < node_info[b][0]:
        b = node_info[b][1]
    while a != b:
        a = node_info[a][1]
        b = node_info[b][1]
    print(a)