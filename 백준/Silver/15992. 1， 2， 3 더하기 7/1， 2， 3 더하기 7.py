T = int(input())
arr = [[0] * 1001 for _ in range(3)]
arr[0][0] = 1
arr[1][1] = 1
arr[2][1] = 1
arr[2][2] = 1
i = 3
while i <= 1000:
    lst = [0] * 1001
    for j in range(1, 1001):
        lst[j] = (arr[-1][j - 1] + arr[-2][j - 1] + arr[-3][j - 1]) % 1000000009
    arr.append(lst)
    i += 1
for _ in range(T):
    n, m = map(int, input().split())
    print(arr[n][m])