def change(i, visited, a):
    global ans
    if a >= ans:
        return
    if i == n:
        if a < ans:
            ans = a
        return
    for j in range(n):
        if not visited[j]:
            visited[j] = True
            change(i + 1, visited, a + abs(bf[i][0] - af[j][0]) + abs(bf[i][1] - af[j][1]))
            visited[j] = False

before = []
for _ in range(4):
    before.append(list(input()))
input()
after = []
for _ in range(4):
    after.append(list(input()))
diff = [[0] * 4 for _ in range(4)]
bf = []
af = []
n = 0
for i in range(4):
    for j in range(4):
        if before[i][j] != after[i][j]:
            if before[i][j] == 'L':
                n += 1
                bf.append([i, j])
            else:
                af.append([i, j])
visited = [False] * n
ans = 32
change(0, visited, 0)
print(ans)