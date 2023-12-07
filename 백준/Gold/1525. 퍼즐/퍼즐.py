import copy
from collections import deque

puz = []
ans = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
for _ in range(3):
    puz.append(list(map(int, input().split())))
for i in range(3):
    for j in range(3):
        if puz[i][j] == 0:
            zero = [i, j]
visited = set()
stat = deque([[0, puz, zero]])
while stat:
    n, s, z = stat.popleft()
    if s == ans:
        print(n)
        break
    visited.add(str(s))
    if z[0] != 0:
        n_s = copy.deepcopy(s)
        n_s[z[0]][z[1]] = s[z[0] - 1][z[1]]
        n_s[z[0] - 1][z[1]] = 0
        if str(n_s) not in visited:
            stat.append([n + 1, n_s, [z[0] - 1, z[1]]])
            visited.add(str(n_s))
    if z[0] != 2:
        n_s = copy.deepcopy(s)
        n_s[z[0]][z[1]] = s[z[0] + 1][z[1]]
        n_s[z[0] + 1][z[1]] = 0
        if str(n_s) not in visited:
            stat.append([n + 1, n_s, [z[0] + 1, z[1]]])
            visited.add(str(n_s))
    if z[1] != 0:
        n_s = copy.deepcopy(s)
        n_s[z[0]][z[1]] = s[z[0]][z[1] - 1]
        n_s[z[0]][z[1] - 1] = 0
        if str(n_s) not in visited:
            stat.append([n + 1, n_s, [z[0], z[1] - 1]])
            visited.add(str(n_s))
    if z[1] != 2:
        n_s = copy.deepcopy(s)
        n_s[z[0]][z[1]] = s[z[0]][z[1] + 1]
        n_s[z[0]][z[1] + 1] = 0
        if str(n_s) not in visited:
            stat.append([n + 1, n_s, [z[0], z[1] + 1]])
            visited.add(str(n_s))
else:
    print(-1)