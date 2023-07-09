import copy

def find_set(i):
    global visited
    hap1 = 0
    lst1 = []
    hap2 = w_lst[i-1]
    lst2 = [i]
    for i1 in t_connect[i]:
        if visited[i1]:
            a, b = visited[i1]
        else:
            a, b = find_set(i1)
        hap1 += a
        lst1 += b
        for i2 in t_connect[i1]:
            if visited[i2]:
                a, b = visited[i2]
            else:
                a, b = find_set(i2)
            hap2 += a
            lst2 += b
    if hap1 > hap2:
        visited[i] = [hap1, lst1]
        return hap1, lst1
    else:
        visited[i] = [hap2, lst2]
        return hap2, lst2

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
visited = [False] * (n+1)
a, b = find_set(1)
b.sort()
print(a)
print(*b)