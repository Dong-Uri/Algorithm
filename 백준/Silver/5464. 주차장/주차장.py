import sys
input = sys.stdin.readline

N, M = map(int, input().split())
R = []
for _ in range(N):
    R.append(int(input()))
W = []
for _ in range(M):
    W.append(int(input()))
full = [False] * N
empty = N
where = [False] * M
que = []
ans = 0
for _ in range(2 * M):
    i = int(input())
    if i > 0:
        i -= 1
        if empty:
            empty -= 1
            for j in range(N):
                if not full[j]:
                    full[j] = True
                    where[i] = j
                    ans += R[j] * W[i]
                    break
        else:
            que.append(i)
    else:
        i = -i - 1
        if que:
            j = where[i]
            i = que.pop(0)
            where[i] = j
            ans += R[j] * W[i]
        else:
            empty += 1
            full[where[i]] = False
print(ans)