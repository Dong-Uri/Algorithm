T = int(input())
arr = [1, 1, 2]
i = 3
while i <= 100000:
    arr.append((arr[-1] + arr[-2] + arr[-3]) % 1000000009)
    i += 1
new_arr = [1, 1, 2]
i = 3
while i <= 100000:
    if i % 2:
        new_arr.append((arr[(i - 1) // 2] + arr[(i - 3) // 2]) % 1000000009)
    else:
        new_arr.append((arr[i // 2] + arr[(i - 2) // 2]) % 1000000009)
    i += 1
for _ in range(T):
    n = int(input())
    print(new_arr[n])