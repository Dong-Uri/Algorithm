n = int(input())
stat = [[0] * n for _ in range(3)]
for i in range(n):
    w = int(input())
    if i == 0:
        stat[1][0] = w
        stat[2][0] = w
    else:
        stat[0][i] = max(stat[1][i-1], stat[2][i-1])
        stat[1][i] = max(stat[0][i], stat[0][i-1] + w)
        stat[2][i] = max(stat[1][i], stat[1][i-1] + w)
print(stat[-1][-1])