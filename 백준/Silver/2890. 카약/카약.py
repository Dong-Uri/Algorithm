R, C = map(int, input().split())
far = [[0, 0]] * 10
for _ in range(R):
    line = input()
    for i in range(C):
        if line[-1 - i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            far[int(line[-1 - i])] = [i, int(line[-1 - i])]
            break
far.sort()
ans = [0] * 10
rate = 0
f_before = 0
for f, n in far:
    if f == f_before:
        ans[n] = rate
    else:
        f_before = f
        rate += 1
        ans[n] = rate
for i in range(1, 10):
    print(ans[i])