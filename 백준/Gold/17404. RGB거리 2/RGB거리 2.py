import copy
import sys
N = int(sys.stdin.readline().rstrip())
lst = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
lst1 = copy.deepcopy(lst)
lst2 = copy.deepcopy(lst)
lst3 = copy.deepcopy(lst)
lst1[0][1] = lst1[0][2] = lst2[0][0] = lst2[0][2] = lst3[0][0] = lst3[0][1] = 1000
for i in range(1, N):
    lst1[i][0] += min(lst1[i - 1][1], lst1[i - 1][2])
    lst1[i][1] += min(lst1[i - 1][0], lst1[i - 1][2])
    lst1[i][2] += min(lst1[i - 1][1], lst1[i - 1][0])
    lst2[i][0] += min(lst2[i - 1][1], lst2[i - 1][2])
    lst2[i][1] += min(lst2[i - 1][0], lst2[i - 1][2])
    lst2[i][2] += min(lst2[i - 1][1], lst2[i - 1][0])
    lst3[i][0] += min(lst3[i - 1][1], lst3[i - 1][2])
    lst3[i][1] += min(lst3[i - 1][0], lst3[i - 1][2])
    lst3[i][2] += min(lst3[i - 1][1], lst3[i - 1][0])
print(min(lst1[N-1][1], lst1[N-1][2], lst2[N-1][0], lst2[N-1][2], lst3[N-1][1], lst3[N-1][0]))