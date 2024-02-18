N = int(input())
a_list = list(map(int, input().split()))
a_dict = {}
for a in a_list:
    if a not in a_dict.keys():
        a_dict[a] = 0
    a_dict[a] += 1
for n in a_dict.values():
    if n > (N + 1) // 2:
        print('NO')
        break
else:
    print('YES')