N, K = map(int, input().split())
dolls = list(map(int, input().split()))
lion = []
for i in range(N):
    if dolls[i] == 1:
        lion.append(i)
if len(lion) < K:
    print(-1)
else:
    ans = N
    for i in range(len(lion) - K + 1):
        if lion[i + K - 1] - lion[i] + 1 < ans:
            ans = lion[i + K - 1] - lion[i] + 1
    print(ans)