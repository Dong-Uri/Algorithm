def get_apple(i, a, node_set):
    global ans
    if i == apple_n:
        if a > ans:
            ans = a
        return
    get_apple(i+1, a, node_set)
    new_node_set = node_set.union(apple_lst[i])
    if len(new_node_set) <= k:
        get_apple(i+1, a+1, new_node_set)


n, k = map(int, input().split())
parent = [[] for _ in range(n)]
for _ in range(n-1):
    p, c = map(int, input().split())
    parent[c] = p
apple = list(map(int, input().split()))
apple_lst = []
apple_n = 0
for i in range(n):
    if apple[i]:
        connect = {0}
        while i:
            connect.add(i)
            i = parent[i]
        apple_lst.append(connect)
        apple_n += 1
ans = 0
get_apple(0, 0, {0})
print(ans)