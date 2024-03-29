import sys

def cnt(x, y):
    return max((x - x // 2) * y, x * (y - y // 2))

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    X, Y, x, y = map(int, sys.stdin.readline().rstrip().split())
    XX, xx = divmod(X, x)
    YY, yy = divmod(Y, y)
    ans = 0
    ans += cnt(XX + 1, YY + 1) * xx * yy
    ans += cnt(XX + 1, YY) * xx * (y - yy)
    ans += cnt(XX, YY + 1) * (x - xx) * yy
    ans += cnt(XX, YY) * (x - xx) * (y - yy)
    print(ans)