import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
cnt = min(N, M) // 2
lsts = [deque() for _ in range(cnt)]
for i in range(cnt):
    lsts[i] += arr[i][i:M-i]
    for j in range(i+1, N-i-1):
        lsts[i].append(arr[j][M-i-1])
    lsts[i] += arr[N-i-1][i:M-i][::-1]
    for j in range(N-i-2, i, -1):
        lsts[i].append(arr[j][i])
for i in range(cnt):
    lsts[i].rotate(-R)
    j = 0
    arr[i][i] = lsts[i][j]
    chng = [i, i+1]
    while chng != [i, i]:
        j += 1
        arr[chng[0]][chng[1]] = lsts[i][j]
        if chng[1] == i:
            chng[0] -= 1
        elif chng[0] == N-i-1:
            chng[1] -= 1
        elif chng[1] == M-i-1:
            chng[0] += 1
        elif chng[0] == i:
            chng[1] += 1
        else:
            print('somthing wrong')
for line in arr:
    print(*line)