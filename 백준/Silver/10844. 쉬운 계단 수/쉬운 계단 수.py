N = int(input())
ans = [0] + [1] * 9
n = 1
while n < N:
    n += 1
    newans = [0] * 10
    for i in range(9):
        newans[i] += ans[i+1]
    for i in range(1,10):
        newans[i] += ans[i-1]
    ans = newans
print(sum(ans) % 1000000000)