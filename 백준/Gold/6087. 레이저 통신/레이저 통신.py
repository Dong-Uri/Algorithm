W, H = map(int, input().split())
zido = []
SE = []
for i in range(H):
    line = input()
    j = line.find('C')
    if j != -1:
        SE.append([i, j])
        more = line[j + 1:].find('C')
        if more != -1:
            j += more + 1
            SE.append([i, j])
    zido.append(line)
visited = [[-1] * W for _ in range(H)]
visited[SE[0][0]][SE[0][1]] = 0
now = [SE[0] + [0], SE[0] + [1]]
answer = 0
while now and not answer:
    n = now.pop(0)
    v = visited[n[0]][n[1]]
    if n[2]:
        new = [n[0], n[1]]
        while True:
            new[0] -= 1
            if new[0] == -1:
                break
            if zido[new[0]][new[1]] == '*':
                break
            if visited[new[0]][new[1]] != -1:
                continue
            if new == SE[1]:
                answer = v
                break
            visited[new[0]][new[1]] = v + 1
            now.append(new + [0])
        new = [n[0], n[1]]
        while True:
            new[0] += 1
            if new[0] == H:
                break
            if zido[new[0]][new[1]] == '*':
                break
            if visited[new[0]][new[1]] != -1:
                continue
            if new == SE[1]:
                answer = v
                break
            visited[new[0]][new[1]] = v + 1
            now.append(new + [0])
    else:
        new = [n[0], n[1]]
        while True:
            new[1] -= 1
            if new[1] == -1:
                break
            if zido[new[0]][new[1]] == '*':
                break
            if visited[new[0]][new[1]] != -1:
                continue
            if new == SE[1]:
                answer = v
                break
            visited[new[0]][new[1]] = v + 1
            now.append(new + [1])
        new = [n[0], n[1]]
        while True:
            new[1] += 1
            if new[1] == W:
                break
            if zido[new[0]][new[1]] == '*':
                break
            if visited[new[0]][new[1]] != -1:
                continue
            if new == SE[1]:
                answer = v
                break
            visited[new[0]][new[1]] = v + 1
            now.append(new + [1])
print(answer)