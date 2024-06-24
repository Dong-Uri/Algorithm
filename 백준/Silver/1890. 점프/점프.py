N = int(input())
pan = []
for _ in range(N):
    pan.append(list(map(int, input().split())))
cnt = [[0] * N for _ in range(N)]
cnt[0][0] = 1
for i in range(N):
    for j in range(N):
        if cnt[i][j] and pan[i][j]:
            if i + pan[i][j] < N:
                cnt[i + pan[i][j]][j] += cnt[i][j]
            if j + pan[i][j] < N:
                cnt[i][j + pan[i][j]] += cnt[i][j]
print(cnt[-1][-1])