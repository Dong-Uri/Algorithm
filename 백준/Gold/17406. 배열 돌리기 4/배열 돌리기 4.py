import sys
from collections import deque
import itertools
import copy

def get_lists(r, c, s, arr):
    lsts = [deque() for _ in range(s)]
    for i in range(s):
        lsts[i] += arr[r-s+i-1][c-s+i-1:c+s-i-1]
        for j in range(r-s+i-1, r+s-i-1):
            lsts[i].append(arr[j][c+s-i-1])
        lsts[i] += arr[r+s-i-1][c+s-i-1:c-s+i-1:-1]
        for j in range(r+s-i-1, r-s+i-1, -1):
            lsts[i].append(arr[j][c-s+i-1])
    return lsts

def get_ans(arr, rots):
    global answer
    for rot in rots:
        lsts = get_lists(rot[0], rot[1], rot[2], arr)
        for i in range(rot[2]):
            lsts[i].rotate(1)
            j = 0
            chng = [rot[0]-rot[2]+i-1, rot[1]-rot[2]+i-1]
            arr[chng[0]][chng[1]] = lsts[i][j]
            chng[1] += 1
            while chng != [rot[0]-rot[2]+i-1, rot[1]-rot[2]+i-1]:
                j += 1
                arr[chng[0]][chng[1]] = lsts[i][j]
                if chng[1] == rot[1]-rot[2]+i-1:
                    chng[0] -= 1
                elif chng[0] == rot[0]+rot[2]-i-1:
                    chng[1] -= 1
                elif chng[1] == rot[1]+rot[2]-i-1:
                    chng[0] += 1
                elif chng[0] == rot[0]-rot[2]+i-1:
                    chng[1] += 1
                else:
                    print('somthing wrong')
    for line in arr:
        if sum(line) < answer:
            answer = sum(line)

N, M, K = map(int, sys.stdin.readline().rstrip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
rots = []
for _ in range(K):
    rots.append(list(map(int, sys.stdin.readline().rstrip().split())))
rots_lst = itertools.permutations(rots, K)
answer = 5000
for rots in rots_lst:
    ans = copy.deepcopy(arr)
    get_ans(ans, rots)
print(answer)