N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())
ans = 0
for s in sizes:
    ans += s // T
    if s % T:
        ans += 1
print(ans)
print(N // P, N % P)