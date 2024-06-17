from collections import deque
import sys

def print_ans(L):
    if L:
        L.sort()
        print(*L)
    else:
        print('None')

n = int(sys.stdin.readline().rstrip())
A = []
B = []
C = []
wait = deque()
for _ in range(n):
    info = list(map(int, sys.stdin.readline().rstrip().split()))
    if info[0] == 1:
        wait.append(info)
    if info[0] == 2:
        stu = wait.popleft()
        if stu[2] == info[1]:
            A.append(stu[1])
        else:
            B.append(stu[1])
for stu in wait:
    C.append(stu[1])
print_ans(A)
print_ans(B)
print_ans(C)