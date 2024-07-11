A, B = map(int, input().split())
arr = []
i = 1
while len(arr) < 1000:
    for _ in range(i):
        arr.append(i)
    i += 1
print(sum(arr[A - 1:B]))