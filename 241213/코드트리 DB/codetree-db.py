import heapq
from bisect import bisect_left, bisect_right, insort

Q = int(input())
for _ in range(Q):
    q = input().split()
    
    if q[0] == 'init':
        name_dict = {}
        value_dict = {}
        value_sort = [0, 1000000001]  # 경계값 유지
    
    elif q[0] == 'insert':
        name = q[1]
        value = int(q[2])
        if name in name_dict or value in value_dict:
            print(0)
        else:
            name_dict[name] = value
            value_dict[value] = name
            insort(value_sort, value)  # 정렬된 위치에 삽입
            print(1)
    
    elif q[0] == 'delete':
        name = q[1]
        if name not in name_dict:
            print(0)
        else:
            value = name_dict.pop(name)
            value_dict.pop(value)
            value_sort.remove(value)  # 리스트에서 삭제
            print(value)
    
    elif q[0] == 'rank':
        k = int(q[1])
        if k >= len(value_sort) - 1:  # 유효한 k 확인
            print('None')
        else:
            print(value_dict[value_sort[k]])
    
    elif q[0] == 'sum':
        k = int(q[1])
        idx = bisect_right(value_sort, k)  # k 이하의 값까지의 합 계산
        print(sum(value_sort[:idx]))

    # print(q)
    # print(name_dict)
    # print(value_dict)
    # print(value_sort)