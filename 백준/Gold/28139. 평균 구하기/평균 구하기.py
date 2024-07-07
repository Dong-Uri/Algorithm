N = int(input())
xys = []
for _ in range(N):
    xys.append(list(map(int, input().split())))
ans = 0
for i in range(N):
    for j in range(i):
        x = xys[i][0] - xys[j][0]
        y = xys[i][1] - xys[j][1]
        ans += (x ** 2 + y ** 2) ** 0.5
print(ans * 2 / N)