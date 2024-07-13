import sys
input = sys.stdin.readline

def give_rd(i, p, x, y):
    global flag, ans
    if flag:
        return
    if x > E:
        return
    if p == P:
        if x <= E and E <= y:
            flag = True
            return
        return
    if i == N:
        return
    give_rd(i + 1, p, x, y)
    if flag:
        return
    ans[i] = True
    give_rd(i + 1, p + 1, x + members[i][0], y + members[i][1])
    if flag:
        return
    ans[i] = False

N, P, E = map(int, input().split())
members = []
for _ in range(N):
    members.append(list(map(int, input().split())))
flag = False
ans = [False] * N
give_rd(0, 0, 0, 0)
if not flag:
    print(-1)
else:
    answer = [0] * N
    for i in range(N):
        if ans[i]:
            answer[i] = members[i][0]
            E -= members[i][0]
    i = 0
    while E:
        if not ans[i]:
            i += 1
        elif members[i][1] == answer[i]:
            i += 1
        else:
            E -= 1
            answer[i] += 1
    print(*answer)