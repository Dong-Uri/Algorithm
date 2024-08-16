T = int(input())
arr = [
    [],
    [1, 0, 0], # 1
    [0, 1, 0], # 2
    [1, 1, 1], # 1+2, 2+1, 3
]
i = 4
while i <= 100000:
    lst = []
    lst.append((arr[-1][1] + arr[-1][2]) % 1000000009)
    lst.append((arr[-2][0] + arr[-2][2]) % 1000000009)
    lst.append((arr[-3][0] + arr[-3][1]) % 1000000009)
    arr.append(lst)
    i += 1
for _ in range(T):
    n = int(input())
    print(sum(arr[n]) % 1000000009)