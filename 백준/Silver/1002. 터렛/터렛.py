T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    hap = r1 + r2
    cha = abs(r1 - r2)
    r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)
    if r == 0 and cha == 0:
        if hap == 0:
            ans = 1
        else:
            ans = -1
    elif r > hap or r < cha:
        ans = 0
    elif r == hap or r == cha:
        ans = 1
    else:
        ans = 2
    print(ans)