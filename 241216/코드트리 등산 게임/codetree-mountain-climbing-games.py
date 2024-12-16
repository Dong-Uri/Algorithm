# 3 2 5 7 8 5 3 1 10 8
# 0 0 1 2 3 1 1 0 4 3

# 0: 3 2 1
# 1: 5 5 3
# 2: 7
# 3: 8 8
# 4: 10

Q = int(input())
for _ in range(Q):
    order = list(map(int, input().split()))

    if order[0] == 100:
        n = order[1]
        mountain_list = []
        mountain_info = []
        for i in range(2, n + 2):
            h = order[i]
            t = len(mountain_info)
            while True:
                if t > 0 and h > mountain_info[t - 1][-1]:
                    mountain_list.append([t, h])
                    if t == len(mountain_info):
                        mountain_info.append([h])
                    else:
                        mountain_info[t].append(h)
                    break
                if t == 0:
                    mountain_list.append([t, h])
                    if mountain_info:
                        mountain_info[t].append(h)
                    else:
                        mountain_info.append([h])
                    break
                t -= 1

    if order[0] == 200:
        h = order[1]
        t = len(mountain_info)
        while True:
            if t > 0 and h > mountain_info[t - 1][-1]:
                mountain_list.append([t, h])
                if t == len(mountain_info):
                    mountain_info.append([h])
                else:
                    mountain_info[t].append(h)
                break
            if t == 0:
                mountain_list.append([t, h])
                if mountain_info:
                    mountain_info[t].append(h)
                else:
                    mountain_info.append([h])
                break
            t -= 1

    if order[0] == 300:
        i, _ = mountain_list.pop()
        mountain_info[i].pop()
        if not mountain_info[i]:
            mountain_info.pop()

    if order[0] == 400:
        m = order[1]
        ans = 0
        ans += mountain_list[m - 1][0] * 1000000
        ans += 1000000
        ans += (len(mountain_info) - 1) * 1000000
        ans += mountain_info[-1][0]
        print(ans)