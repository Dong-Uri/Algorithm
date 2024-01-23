import copy
def solution(info, edges):
    ch1 = [0] * len(info)
    ch2 = [0] * len(info)
    prt = [0] * len(info)
    for e in edges:
        if ch1[e[0]] == 0:
            ch1[e[0]] = e[1]
        else:
            ch2[e[0]] = e[1]
        prt[e[1]] = e[0]

    def cnt(n):
        nonlocal sheep
        nonlocal wolf
        nonlocal nodes
        while True:
            nodes.append(n)
            if info[n]:
                wolf += 1
            else:
                sheep += 1
            if n == 0:
                break
            n = prt[n]

    while True:
        no_wolf = True
        for i in range(len(info)):
            if ch1[i] == 0 and ch2[i] == 0 and info[i] == 1:
                no_wolf = False
                if ch1[prt[i]] == i:
                    ch1[prt[i]] = 0
                elif ch2[prt[i]] == i:
                    ch2[prt[i]] = 0
                info[i] = -1
        if no_wolf:
            break

    prt_info = []
    for i in range(len(info)):
        if info[i] == 0:
            sheep = wolf = 0
            nodes = []
            cnt(i)
            prt_info.append([nodes, sheep, wolf])

    sheep = wolf = 0
    while prt_info:
        prt_info.sort(key=lambda x: (-x[2], x[1]))
        if prt_info[-1][1] < prt_info[-1][2]:
            break
        n_prt_info = copy.deepcopy(prt_info)
        w = wolf
        s = sheep
        get = n_prt_info.pop()
        end = False
        while get[0]:
            go = get[0].pop()
            empty = False
            if info[go]:
                w += 1
            else:
                s += 1
            for p in n_prt_info:
                if go == p[0][-1]:
                    p[0].pop()
                    if info[go]:
                        p[2] -= 1
                    else:
                        p[1] -= 1
                    if not p[0]:
                        empty = True
            if empty:
                n_prt_info.remove([[], 0, 0])
            if w >= s:
                end = True
                break
        if end:
            break
        prt_info = n_prt_info
        wolf = w
        sheep = s

    def perm(n, k):
        if n == k:
            prt_info_lst.append(copy.deepcopy(prt_info))
        else:
            for i in range(n, k):
                prt_info[n], prt_info[i] = prt_info[i], prt_info[n]
                perm(n+1, k)
                prt_info[n], prt_info[i] = prt_info[i], prt_info[n]

    prt_info = [x for x in prt_info if sheep + x[1] > wolf + x[2]]
    prt_info_lst = []
    perm(0, len(prt_info))

    max_s = sheep
    for prt_info in prt_info_lst:
        s = sheep
        w = wolf
        while prt_info:
            get = prt_info.pop()
            end = False
            while get[0]:
                go = get[0].pop()
                empty = False
                if info[go]:
                    w += 1
                else:
                    s += 1
                for p in prt_info:
                    if go == p[0][-1]:
                        p[0].pop()
                        if info[go]:
                            p[2] -= 1
                        else:
                            p[1] -= 1
                        if p[0] == []:
                            empty = True
                if empty:
                    prt_info.remove([[], 0, 0])
                if w >= s:
                    end = True
                    break
            if end:
                break
        if s > max_s:
            max_s = s

    return max_s