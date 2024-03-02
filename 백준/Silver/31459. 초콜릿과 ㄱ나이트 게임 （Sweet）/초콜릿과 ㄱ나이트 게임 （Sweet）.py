T = int(input())
for _ in range(T):
    X, Y, x, y = map(int, input().split())
    choco = [[True] * Y for _ in range(X)]
    answer = 0
    for i in range(X):
        for j in range(Y):
            if choco[i][j]:
                ii = i
                jj = j
                TF = True
                while ii < X and jj < Y:
                    choco[ii][jj] = False
                    if TF:
                        answer += 1
                        TF = False
                    else:
                        TF = True
                    ii += x
                    jj += y
    print(answer)
