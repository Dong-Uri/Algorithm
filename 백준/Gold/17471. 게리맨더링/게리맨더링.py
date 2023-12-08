def TF(lst, n):
    global case
    if n == N:
        lst[0] = abs(lst[0])
        case.append(lst)
        return
    TF([lst[0] + ingu[n], lst[1] + [n + 1], lst[2]], n + 1)
    TF([lst[0] - ingu[n], lst[1], lst[2] + [n + 1]], n + 1)

N = int(input())
ingu = list(map(int, input().split()))
connect = [None]
for _ in range(N):
    connect.append(list(map(int, input().split())))
case = []
TF([ingu[0], [1], []], 1)
case.sort()
for c in case:
    if not c[1] or not c[2]:
        continue
    visited = [False] * (N + 1)
    visited[c[1][0]] = True
    now = [c[1][0]]
    while now:
        n = now.pop(0)
        for m in connect[n][1:]:
            if m in c[1] and not visited[m]:
                visited[m] = True
                now.append(m)
    visited[c[2][0]] = True
    now = [c[2][0]]
    while now:
        n = now.pop(0)
        for m in connect[n][1:]:
            if m in c[2] and not visited[m]:
                visited[m] = True
                now.append(m)
    for v in visited[1:]:
        if not v:
            break
    else:
        print(c[0])
        break
else:
    print(-1)
