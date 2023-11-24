def solution(queue1, queue2):
    from collections import deque
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = -1
    l = len(queue1)
    sum_1 = sum(queue1)
    sum_2 = sum(queue2)
    if (sum_1 + sum_2) % 2:
        return -1
    cnt = 0
    while cnt < l * 3:
        if not queue1 or not queue2:
            return -1
        if sum_1 == sum_2:
            return cnt
        if sum_1 > sum_2:
            n = queue1.popleft()
            queue2.append(n)
            sum_1 -= n
            sum_2 += n
        else:
            n = queue2.popleft()
            queue1.append(n)
            sum_2 -= n
            sum_1 += n
        cnt += 1
    return -1