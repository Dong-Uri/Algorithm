N, M = map(int, input().split())
line6, line1 = 1000, 1000
for _ in range(M):
    a, b = map(int, input().split())
    if a < line6:
        line6 = a
    if b < line1:
        line1 = b
if line1 * 6 < line6:
    print(N * line1)
else:
    ans = N // 6 * line6
    N %= 6
    ans += min(N * line1, line6)
    print(ans)