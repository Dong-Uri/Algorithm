N = int(input())
ans = [[0] + [1] * 8 + [0]] + [[0] * 10] + [[0] * 9 + [1]] + [[0] * 10]
# take none, take 0, take 9, take all
n = 1
while n < N:
    n += 1
    newans = [[0] * 10 for _ in range(4)]
    for i in range(4):
        for j in range(1,9):
            newans[i][j] += ans[i][j-1] + ans[i][j+1]
    newans[1][0] = ans[0][1] + ans[1][1]
    newans[2][9] = ans[0][8] + ans[2][8]
    newans[3][0] = ans[2][1] + ans[3][1]
    newans[3][9] = ans[1][8] + ans[3][8]
    ans = newans
print(sum(ans[3]) % 1000000000)