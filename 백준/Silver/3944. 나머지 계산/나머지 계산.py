import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    B, D = sys.stdin.readline().rstrip().split()
    ans = 0
    for d in D:
        ans += int(d)
    print(ans % (int(B) - 1))