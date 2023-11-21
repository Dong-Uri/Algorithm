N = int(input())
ans = [[0] * 3 for _ in range(2)]
# 전체 L의 개수, 기존 연속 A의 개수
ans[0][0] = ans[1][0] = ans[0][1] = 1
for _ in range(1, N):
    newans = [[0] * 3 for _ in range(2)]
    newans[0][0] = sum(ans[0])
    newans[0][1] = ans[0][0]
    newans[0][2] = ans[0][1]
    newans[1][0] = sum(ans[1]) + newans[0][0]
    newans[1][1] = ans[1][0]
    newans[1][2] = ans[1][1]
    ans = newans
print((sum(ans[0]) + sum(ans[1])) % 1000000)