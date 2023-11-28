N, B = map(int, input().split())
ans = [[0] + [1] * (B - 2) + [0]] + [[0] * B] + [[0] * (B - 1) + [1]] + [[0] * B]
# take none, take 0, take last, take all
n = 1
while n < N:
    n += 1
    newans = [[0] * B for _ in range(4)]
    for i in range(4):
        for j in range(1, B - 1):
            newans[i][j] += (ans[i][j-1] + ans[i][j+1]) % 1000000000
    newans[1][0] = (ans[0][1] + ans[1][1]) % 1000000000
    newans[2][B - 1] = (ans[0][B - 2] + ans[2][B - 2]) % 1000000000
    newans[3][0] = (ans[2][1] + ans[3][1]) % 1000000000
    newans[3][B - 1] = (ans[1][B - 2] + ans[3][B - 2]) % 1000000000
    ans = newans
print(sum(ans[3]) % 1000000000)