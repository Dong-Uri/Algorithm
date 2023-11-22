T = int(input())
for _ in range(T):
    N = int(input())
    MBTI = list(input().split())
    lst = [0] * 16
    ans = 12
    for i in range(N):
        idx = 0
        for x in range(4):
            if MBTI[i][x] == 'I':
                idx += 1
            if MBTI[i][x] == 'N':
                idx += 2
            if MBTI[i][x] == 'F':
                idx += 4
            if MBTI[i][x] == 'J':
                idx += 8
        lst[idx] += 1
        if lst[idx] == 3:
            ans = 0
            break
    if ans:
        for i in range(N):
            for j in range(i+1, N):
                d1 = 0
                for x in range(4):
                    if MBTI[i][x] != MBTI[j][x]:
                        d1 += 1
                for k in range(j+1, N):
                    d2 = 0
                    for x in range(4):
                        if MBTI[i][x] != MBTI[k][x]:
                            d2 += 1
                    d3 = 0
                    for x in range(4):
                        if MBTI[j][x] != MBTI[k][x]:
                            d3 += 1
                    if d1 + d2 + d3 < ans:
                            ans = d1 + d2 + d3
    print(ans)