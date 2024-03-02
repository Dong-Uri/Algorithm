T = int(input())
for _ in range(T):
    line = input()
    cases = [0, 0]
    for l in line:
        if l == 'H':
            cases[0] += 1
        if l == '?':
            cases[1] += 1
    swch = cases[0] % 2
    if cases[1] == 0:
        if swch:
            answer = 1
        else:
            answer = 0
    else:
        answer = 1
        for _ in range(cases[1] - 1):
            answer *= 2
            answer %= 1e9 + 7
    print(int(answer))