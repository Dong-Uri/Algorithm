T = int(input())
arr = [
    [0, 1],
    [1, 0],
    [1, 1],
]
i = 3
while i <= 100000:
    lst = [0, 0]
    lst[0] = (arr[-1][1] + arr[-2][1] + arr[-3][1]) % 1000000009
    lst[1] = (arr[-1][0] + arr[-2][0] + arr[-3][0]) % 1000000009
    arr.append(lst)
    i += 1
for _ in range(T):
    n = int(input())
    print(*arr[n])