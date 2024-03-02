N = int(input())
choco = []
TF = []
for i in range(N):
    line = input()
    choco.append(line)
    TF.append([True] * (i + 1) + [False] * (N - i))
TF.append([False] * (N + 1))
answer = 1
for i in range(N):
    for j in range(N):
        if TF[i][j]:
            TF[i][j] = False
            if choco[i][j] == 'R':
                if TF[i + 1][j] and TF[i + 1][j + 1] and choco[i + 1][j] == 'R' and choco[i + 1][j + 1] == 'R':
                    TF[i + 1][j] = False
                    TF[i + 1][j + 1] = False
                else:
                    answer = 0
                    break
            if choco[i][j] == 'B':
                if TF[i][j + 1] and TF[i + 1][j + 1] and choco[i][j + 1] == 'B' and choco[i + 1][j + 1] == 'B':
                    TF[i][j + 1] = False
                    TF[i + 1][j + 1] = False
                else:
                    answer = 0
                    break
    if not answer:
        break
print(answer)