A, B, C, D, E = map(int, input().split())
ans = 0
while E:
    ans += 1
    E -= 1
while D:
    ans += 1
    D -= 1
    if A > 0:
        A -= 1
while C:
    ans += 1
    C -= 1
    if B > 0:
        B -= 1
    elif A > 1:
        A -= 2
    elif A == 1:
        A = 0
while B:
    ans += 1
    if B > 1:
        B -= 2
        if A > 0:
            A -= 1
    elif B == 1:
        B -= 1
        if A > 2:
            A -= 3
        elif A > 0:
            A = 0
while A:
    ans += 1
    if A > 4:
        A -= 5
    elif A > 0:
        A = 0
print(ans)