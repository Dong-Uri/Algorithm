S = input()
T = input()
a, b, c = 0, len(T), 1
while b - a > len(S):
    if c == 1:
        b -= 1
        if T[b] == 'B':
            c = -1
    else:
        a += 1
        if T[a - 1] == 'B':
            c = 1
if S == T[a:b][::c]:
    print(1)
else:
    print(0)