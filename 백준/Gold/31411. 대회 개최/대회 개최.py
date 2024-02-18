N, K = map(int, input().split())
alg = list(map(int, input().split()))
alg.sort()
curve = [[i, i] for i in alg]
for _ in range(N-1):
    alg = list(map(int, input().split()))
    alg.sort()
    i = 0
    j = 0
    n_curve = []
    while i < len(curve) and j < K:
        if curve[i][0] < alg[j]:
            n_curve.append([curve[i][0], max(curve[i][1], alg[j])])
            i += 1
        elif curve[i][0] > alg[j]:
            n_curve.append([alg[j], curve[i][1]])
            j += 1
        else:
            n_curve.append(curve[i])
            i += 1
            j += 1
    curve = [n_curve.pop()]
    while n_curve:
        c = n_curve.pop()
        if c[1] < curve[-1][1]:
            curve.append(c)
    curve.sort()
answer = 10 ** 5
for c in curve:
    if c[1] - c[0] < answer:
        answer = c[1] - c[0]
print(answer)