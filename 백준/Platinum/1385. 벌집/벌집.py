def find_end(n, group, level, method):
    if group == 8:
        group = 2
    if group == 1:
        group = 7
    fronts = [group]
    add_n = group + 4
    for _ in range(max_level):
        fronts.append(fronts[-1] + add_n)
        add_n += 6
    backs = [group]
    add_n = group + 5
    for _ in range(max_level):
        backs.append(backs[-1] + add_n)
        add_n += 6
    # print(fronts, backs)
    ways = {}
    if method == 'front':
        line = []
        back_n = backs[level - 1] - n
        front_n = n - fronts[level - 1]
        for i in range(front_n + 1):
            line.append(backs[level - 1 - i] - back_n)
        # print(line)
        for i in range(level - front_n):
            ways[fronts[i]] = fronts[i:back_n] + line[::-1]
        for i in range(level - front_n, level):
            w = []
            for j in range(i - back_n):
                w.append(fronts[i] + j)
            ways[fronts[i]] = w + line[level - i - 1::-1]
        for i in range(level, max_level):
            ways[fronts[i]] = [fronts[i]] + ways[fronts[i - 1]]
        # pprint(ways)
    if method == 'back':
        line = []
        back_n = backs[level - 1] - n
        front_n = n - fronts[level - 1]
        for i in range(back_n + 1):
            line.append(fronts[level - 1 - i] + front_n)
        # print(line)
        for i in range(level - back_n):
            ways[backs[i]] = backs[i:front_n] + line[::-1]
        for i in range(level - back_n, level):
            w = []
            for j in range(i - front_n):
                w.append(backs[i] - j)
            ways[backs[i]] = w + line[level - i - 1::-1]
        for i in range(level, max_level):
            ways[backs[i]] = [backs[i]] + ways[backs[i - 1]]
        # pprint(ways)
    if method == 'line':
        ways[group] = [group]
        for i in range(1, max_level + 1):
            front = fronts[i]
            back = backs[i]
            ways[fronts[i]] = []
            ways[backs[i]] = []
            j = 0
            while j <= i:
                j += 1
                ways[fronts[i]].append(front)
                ways[backs[i]].append(back)
                front += 1
                back -= 1
        # pprint(ways)
    return ways

def find_connect(A, B):
    if B == 8:
        B = 2
    if A == 1:
        A = 7
    fronts = [B]
    add_n = B + 4
    for _ in range(max_level - 1):
        fronts.append(fronts[-1] + add_n)
        add_n += 6
    backs = [A]
    add_n = A + 5
    for _ in range(max_level - 1):
        backs.append(backs[-1] + add_n)
        add_n += 6
    ways = {}
    ways[fronts[0]] = [backs[0]]
    ways[backs[max_level - 1]] = [fronts[max_level - 1]]
    for i in range(max_level - 1):
        ways[backs[i]] = [fronts[i], fronts[i + 1]]
        ways[fronts[i + 1]] = [backs[i], backs[i + 1]]
    # pprint(ways)
    return ways

a, b = map(int, input().split())
switch = False
if a > b:
    temp = a
    a = b
    b = temp
    switch = True
point = 2
add_n = 0
group = 0
level = 0
a_info = False
b_info = False
if a == 1:
    a_info = [1, 0]
if b == 1:
    b_info = [1, 0]
while not(a_info and b_info):
    add_n += 1
    level += 1
    for _ in range(6):
        if a >= point and a < point + add_n:
            a_info = [group % 6 + 2, level]
        if b >= point and b < point + add_n:
            b_info = [group % 6 + 2, level]
        group += 1
        point += add_n
chai = (b_info[0] - a_info[0]) % 6
max_level = b_info[1]
if b_info[0] == 1:
    print(1)

elif a_info[0] == 1:
    ways = find_end(b, b_info[0], b_info[1], 'front')
    answer = [1] + ways[b_info[0]]
    if switch:
        answer = answer[::-1]

elif chai == 0:
    fronts = find_end(a, a_info[0], a_info[1], 'front')
    backs = find_end(a, a_info[0], a_info[1], 'back')
    fronts = list(fronts.keys())
    backs = list(backs.keys())
    a_front_n = a - fronts[a_info[1] - 1]
    a_back_n = backs[a_info[1] - 1] - a
    b_front_n = b - fronts[b_info[1] - 1]
    b_back_n = backs[b_info[1] - 1] - b
    if a_front_n >= b_front_n:
        step = a_front_n - b_front_n
        answer = [a]
        for _ in range(step):
            answer.append(answer[-1] - 1)
        for i in range(a_info[1], b_info[1]):
            answer.append(fronts[i] + b_front_n)
    elif a_back_n >= b_back_n:
        step = a_back_n - b_back_n
        answer = [a]
        for _ in range(step):
            answer.append(answer[-1] + 1)
        for i in range(a_info[1], b_info[1]):
            answer.append(backs[i] - b_back_n)
    else:
        answer = [a]
        curve = False
        for i in range(a_info[1], b_info[1]):
            w1 = fronts[i] + a_front_n
            w2 = backs[i] - b_back_n
            if curve:
                answer.append(w2)
            else:
                answer.append(w1)
            if w1 == w2:
                curve = True
    if switch:
        answer = answer[::-1]

elif chai == 1:
    backs = find_end(a, a_info[0], a_info[1], 'back')
    fronts = find_end(b, b_info[0], b_info[1], 'front')
    connects = find_connect(a_info[0], b_info[0])
    ways = {}
    for back in backs.keys():
        for w in connects[back]:
            way = backs[back][::-1] + [w]
            if w not in ways.keys() or len(way) < len(ways[w]):
                ways[w] = way
    answer = []
    for front in fronts.keys():
        ans = ways[front] + fronts[front][1:]
        if not answer or len(ans) < len(answer):
            answer = ans
    if switch:
        answer = answer[::-1]

elif chai == 2:
    backs = find_end(a, a_info[0], a_info[1], 'back')
    connects_1 = find_connect(a_info[0], a_info[0] + 1)
    line = find_end(_, a_info[0] + 1, _, 'line')
    connects_2 = find_connect(b_info[0] - 1, b_info[0])
    fronts = find_end(b, b_info[0], b_info[1], 'front')
    ways_1 = {}
    for back in backs.keys():
        for w in connects_1[back]:
            way = backs[back][::-1] + [w]
            if w not in ways_1.keys() or len(way) < len(ways_1[w]):
                ways_1[w] = way
    for key in ways_1.keys():
        ways_1[key] += line[key][1:]
    ways_2 = {}
    for key, lst in ways_1.items():
        for w in connects_2[lst[-1]]:
            way = ways_1[key] + [w]
            if w not in ways_2.keys() or len(way) < len(ways_2[w]):
                ways_2[w] = way
    answer = []
    for front in fronts.keys():
        ans = ways_2[front] + fronts[front][1:]
        if not answer or len(ans) < len(answer):
            answer = ans
    if switch:
        answer = answer[::-1]

elif chai == 3:
    fronts = find_end(a, a_info[0], a_info[1], 'front')
    backs = find_end(b, b_info[0], b_info[1], 'back')
    answer = fronts[a_info[0]][::-1] + [1] + backs[b_info[0]]
    if switch:
        answer = answer[::-1]

elif chai == 4:
    fronts = find_end(a, a_info[0], a_info[1], 'front')
    connects_1 = find_connect(a_info[0] - 1, a_info[0])
    line = find_end(_, a_info[0] - 1, _, 'line')
    connects_2 = find_connect(b_info[0], b_info[0] + 1)
    backs = find_end(b, b_info[0], b_info[1], 'back')
    ways_1 = {}
    for front in fronts.keys():
        for w in connects_1[front]:
            way = fronts[front][::-1] + [w]
            if w not in ways_1.keys() or len(way) < len(ways_1[w]):
                ways_1[w] = way
    for key in ways_1.keys():
        ways_1[key] += line[key][1:]
    ways_2 = {}
    for key, lst in ways_1.items():
        for w in connects_2[lst[-1]]:
            way = ways_1[key] + [w]
            if w not in ways_2.keys() or len(way) < len(ways_2[w]):
                ways_2[w] = way
    answer = []
    for back in backs.keys():
        ans = ways_2[back] + backs[back][1:]
        if not answer or len(ans) < len(answer):
            answer = ans
    if switch:
        answer = answer[::-1]

elif chai == 5:
    fronts = find_end(a, a_info[0], a_info[1], 'front')
    backs = find_end(b, b_info[0], b_info[1], 'back')
    connects = find_connect(b_info[0], a_info[0])
    ways = {}
    for front in fronts.keys():
        for w in connects[front]:
            way = fronts[front][::-1] + [w]
            if w not in ways.keys() or len(way) < len(ways[w]):
                ways[w] = way
    answer = []
    for back in backs.keys():
        ans = ways[back] + backs[back][1:]
        if not answer or len(ans) < len(answer):
            answer = ans
    if switch:
        answer = answer[::-1]

print(*answer)