num = ['']
for _ in range(3):
    new_num = []
    for n in num:
        for m in range(1, 10):
            m = str(m)
            for nn in n:
                if m == nn:
                    break
            else:
                new_num.append(n + m)
    num = new_num

N = int(input())
for _ in range(N):
    g, s, b = map(int, input().split())
    g = str(g)
    new_num = []
    for n in num:
        ss = 0
        for i in range(3):
            if n[i] == g[i]:
                ss += 1
        if s != ss:
            continue
        bb = 0
        for i in range(3):
            for j in range(3):
                if i != j and n[i] == g[j]:
                    bb += 1
        if b != bb:
            continue
        new_num.append(n)
    num = new_num
print(len(num))