import copy

def find_set(i):
    hap1 = 0
    lst1 = []
    hap2 = w_lst[i-1]
    lst2 = [i]
    for j in t_connect[i]:
        h1, l1, h2, l2 = find_set(j)
        if h1 > h2:
            hap1 += h1
            lst1 += l1
        else:
            hap1 += h2
            lst1 += l2
        hap2 += h1
        lst2 += l1
    return hap1, lst1, hap2, lst2

n = int(input())
w_lst = list(map(int, input().split()))
connect = [[] for _ in range(n+1)]
while True:
    try:
        a, b = map(int, input().split())
        connect[a].append(b)
        connect[b].append(a)
    except:
        break
visited = [False] * (n+1)
t_connect = [[] for _ in range(n+1)]
stack = [1]
visited[1] = True
while stack:
    n_stack = []
    for i in stack:
        for j in connect[i]:
            if not visited[j]:
                visited[j] = True
                t_connect[i].append(j)
                n_stack.append(j)
    stack = copy.deepcopy(n_stack)
hap1, lst1, hap2, lst2 = find_set(1)
if hap1 > hap2:
    print(hap1)
    lst1.sort()
    print(*lst1)
else:
    print(hap2)
    lst2.sort()
    print(*lst2)