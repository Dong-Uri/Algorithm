N = int(input())
ans = [[0] * 10 for _ in range(4)]
# +1, +2, -1, -2
if N == 1:
    print(10)
else:
    base = [1] * 10
    for i in range(1, 10):
        ans[0][i] += base[i-1]
    for i in range(9):
        ans[2][i] += base[i+1]
    n = 2
    while n < N:
        n += 1
        newans = [[0] * 10 for _ in range(4)]
        for i in range(1, 10):
            newans[0][i] += (ans[2][i-1] + ans[3][i-1]) % 1000000007
            newans[1][i] += ans[0][i-1] % 1000000007
        for i in range(9):
            newans[2][i] += (ans[0][i+1] + ans[1][i+1]) % 1000000007
            newans[3][i] += ans[2][i+1] % 1000000007
        ans = newans
    print(sum([sum(ans[i]) for i in range(4)]) % 1000000007)