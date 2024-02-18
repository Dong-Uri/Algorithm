N = int(input())
dirty = []
d = 0
for _ in range(N):
    point = list(map(int, input().split()))
    d += point[1]
    dirty.append(point)
dirty.sort()

d1 = d - dirty[0][1]
d2 = d - dirty[-1][1]
for i in range(N - 1):
    d1 += i * (dirty[i + 1][0] - dirty[i][0])
    d2 += (N - 2 - i) * (dirty[i + 1][0] - dirty[i][0])
answer = min(d1, d2)

for i in range(1, N - 1):
    d1 += dirty[i - 1][1]
    d1 -= dirty[i][1]
    d1 += dirty[i][0] - dirty[i - 1][0]
    if d1 < answer:
        answer = d1
    d2 += dirty[-i][1]
    d2 -= dirty[-i - 1][1]
    d2 += dirty[-i][0] - dirty[-i - 1][0]
    if d2 < answer:
        answer = d2

d1 -= dirty[-1][1]
d1 += dirty[-2][1]
d1 -= (N - 2) * (dirty[-1][0] - dirty[-2][0])
if d1 < answer:
    answer = d1
d2 -= dirty[0][1]
d2 += dirty[1][1]
d2 -= (N - 2) * (dirty[1][0] - dirty[0][0])
if d2 < answer:
    answer = d2

print(answer)