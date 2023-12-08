import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
meats = []
free = 0
for _ in range(N):
    w, c = map(int, sys.stdin.readline().rstrip().split())
    if c == 0:
        free += w
    elif w != 0:
        meats.append([c, -w])
meats.sort()
weight = free
before = 0
ans = 2147483648
if weight >= M:
    ans = 0
for m in meats:
    weight -= m[1]
    if before != m[0]:
        pay = m[0]
    else:
        pay += m[0]
    if weight >= M and pay < ans:
        ans = pay
    before = m[0]
if ans == 2147483648:
    ans = -1
print(ans)