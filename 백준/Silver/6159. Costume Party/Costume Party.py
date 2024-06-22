import sys

N, S = map(int, sys.stdin.readline().rstrip().split())
L = []
for _ in range(N):
    L.append(int(sys.stdin.readline().rstrip()))
L.sort()
l = 0
r = N - 1
ans = 0
while l < r:
    if L[l] + L[r] > S:
        r -= 1
    else:
        ans += r - l
        l += 1
print(ans)