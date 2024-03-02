T = int(input())
for _ in range(T):
    susik = input()
    a = 0
    b = 0
    n = 0
    TF = True
    for s in susik:
        if s == '!':
            if TF:
                a += 1
            else:
                b += 1
        else:
            n = int(s)
            TF = False
    if b:
        n = 1
    if a % 2:
        n = 1 - n
    print(n)