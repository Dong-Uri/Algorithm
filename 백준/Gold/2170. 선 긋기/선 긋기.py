import sys

N = int(sys.stdin.readline().rstrip())
line = []
for _ in range(N):
    line.append(list(map(int, sys.stdin.readline().rstrip().split())))
line.sort()
line_now = line[0]
ans = 0
for l in line[1:]:
    if l[0] > line_now[1]:
        ans += line_now[1] - line_now[0]
        line_now = l
    elif l[1] > line_now[1]:
        line_now[1] = l[1]
ans += line_now[1] - line_now[0]
print(ans)