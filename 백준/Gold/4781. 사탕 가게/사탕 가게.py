import sys

while True:
    n, m = map(float, sys.stdin.readline().rstrip().split())
    if not n:
        break
    dp = [0] * (int(m * 100 + 0.5) + 1)
    candys = []
    for _ in range(int(n)):
        c, p = map(float, sys.stdin.readline().rstrip().split())
        candys.append([int(c), int(p * 100 + 0.5)])
    for i in range(int(m * 100 + 0.5) + 1):
        for c, p in candys:
            if i - p >= 0:
                dp[i] = max(dp[i], dp[i - p] + c)
        dp[i] = max(dp[i - 1], dp[i])
    print(dp[-1])