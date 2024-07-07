def nC2(n):
    return int(n * (n - 1) // 2)

def byens(a, b, n):
    minp = min(a, b)
    maxp = max(a, b)
    if maxp < 0:
        return 0
    if minp >= n:
        return 0
    if maxp >= n:
        maxp = n
    if minp < 0:
        minp = -1
    return nC2(maxp - minp)


n = int(input())
ans = nC2(n + 1) * nC2(n + 1)
xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
if xa == xb:
    ans += byens(ya, yb, n) * (n + 1)
if ya == yb:
    ans += byens(xa, xb, n) * (n + 1)
print(ans)