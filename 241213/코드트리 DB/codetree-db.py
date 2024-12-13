import heapq

Q = int(input())
for _ in range(Q):
    q = list(input().split())

    if q[0] == 'init':
        name_dict = dict()
        value_dict = dict()
        value_sort = [0, 1000000001]

    if q[0] == 'insert':
        name = q[1]
        value = int(q[2])
        if name in name_dict.keys() and name_dict[name]:
            print(0)
            continue
        if value in value_dict.keys() and value_dict[value]:
            print(0)
            continue
        name_dict[name] = value
        value_dict[value] = name
        l = 0
        r = len(value_sort) - 1
        while l + 1 < r:
            if value < value_sort[(l + r) // 2]:
                r = (l + r) // 2
            else:
                l = (l + r) // 2
                if value_sort[l] == value:
                    r = l + 1
        value_sort = value_sort[:l + 1] + [value] + value_sort[r:]
        print(1)
    
    if q[0] == 'delete':
        name = q[1]
        if name not in name_dict.keys() or not name_dict[name]:
            print(0)
            continue
        value = name_dict[name]
        name_dict[name] = 0
        value_dict[value] = 0
        l = 0
        r = len(value_sort) - 1
        while l + 1 < r:
            if value < value_sort[(l + r) // 2]:
                r = (l + r) // 2
            else:
                l = (l + r) // 2
                if value_sort[l] == value:
                    r = l + 1
        value_sort = value_sort[:l] + value_sort[r:]
        print(value)

    if q[0] == 'rank':
        k = int(q[1])
        if k > len(value_sort) - 2:
            print('None')
            continue
        print(value_dict[value_sort[k]])

    if q[0] == 'sum':
        k = int(q[1])
        l = 0
        r = len(value_sort) - 1
        while l + 1 < r:
            if k < value_sort[(l + r) // 2]:
                r = (l + r) // 2
            else:
                l = (l + r) // 2
                if value_sort[l] == k:
                    r = l + 1
        print(sum(value_sort[:l + 1]))