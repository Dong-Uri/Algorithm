import sys

N, M, K = map(int, sys.stdin.readline().rstrip().split())
tile_dict = [[dict() for _ in range(K)] for _ in range(K)]
for n in range(N):
    line = sys.stdin.readline().rstrip()
    for m, a in enumerate(line):
        if a in tile_dict[n % K][m % K].keys():
            tile_dict[n % K][m % K][a] += 1
        else:
            tile_dict[n % K][m % K][a] = 1
ans = N * M
ans_lst = [[None for _ in range(K)] for _ in range(K)]
for i in range(K):
    for j in range(K):
        num = 0
        alpha = None
        for a, x in tile_dict[i][j].items():
            if x > num:
                num = x
                alpha = a
        ans -= num
        ans_lst[i][j] = alpha
print(ans)
for _ in range(N // K):
    for lst in ans_lst:
        line = ''
        for _ in range(M // K):
            for a in lst:
                line += a
        print(line)