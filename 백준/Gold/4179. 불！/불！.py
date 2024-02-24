R, C = map(int, input().split())
miro = []
for _ in range(R):
    line = list(input())
    miro.append(line)
J = []
F = []
for i in range(R):
    for j in range(C):
        if miro[i][j] == 'J':
            J.append([i, j])
        if miro[i][j] == 'F':
            F.append([i, j])
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 0
i = 0
while True:
    i += 1
    nJ = []
    for j in J:
        miro[j[0]][j[1]] = 'V'
        if j[0] == 0 or j[1] == 0 or j[0] == R - 1 or j[1] == C - 1:
            answer = i
            break
        for m in move:
            nj = [j[0] + m[0], j[1] + m[1]]
            if miro[nj[0]][nj[1]] == '.':
                miro[nj[0]][nj[1]] = 'J'
                nJ.append(nj)
    J = nJ
    if answer:
        break
    nF = []
    for f in F:
        for m in move:
            nf = [f[0] + m[0], f[1] + m[1]]
            if nf[0] != -1 and nf[1] != -1 and nf[0] != R and nf[1] != C:
                if miro[nf[0]][nf[1]] == '.':
                    miro[nf[0]][nf[1]] = 'F'
                    nF.append(nf)
                if miro[nf[0]][nf[1]] == 'J':
                    J.remove(nf)
                    miro[nf[0]][nf[1]] = 'F'
                    nF.append(nf)
    F = nF
    if not J:
        answer = 'IMPOSSIBLE'
        break
print(answer)