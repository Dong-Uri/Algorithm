n = int(input())
parent = [[0, 0] for _ in range(n+1)]
child = [[] for _ in range(n+1)]
level = [[i, 0] for i in range(n+1)]
for _ in range(n-1):
    pr, ch, l = map(int, input().split())
    parent[ch] = [pr, l]
    child[pr].append(ch)
stack = [1]
while stack:
    i = stack.pop()
    for j in child[i]:
        level[j][1] = level[i][1] + 1
        stack.append(j)
level.sort(key=lambda x: x[1], reverse=True)
length = [[0, 0] for _ in range(n+1)]
for i, l in level:
    ls = parent[i][1] + max(length[i])
    if length[parent[i][0]][0] <= length[parent[i][0]][1] and ls > length[parent[i][0]][0]:
        length[parent[i][0]][0] = ls
    elif length[parent[i][0]][0] >= length[parent[i][0]][1] and ls > length[parent[i][0]][1]:
        length[parent[i][0]][1] = ls
ans = 0
for a, b in length:
    if a + b > ans:
        ans = a + b
print(ans)