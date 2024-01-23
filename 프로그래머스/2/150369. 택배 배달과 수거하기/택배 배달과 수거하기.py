def solution(cap, n, deliveries, pickups):
    answer = 0
    d_left = n
    p_left = n
    while d_left:
        if deliveries[d_left - 1] == 0:
            d_left -= 1
        else:
            break
    while p_left:
        if pickups[p_left - 1] == 0:
            p_left -= 1
        else:
            break
    while d_left or p_left:
        answer += 2 * max(d_left, p_left)
        d = cap
        while d_left and d:
            if deliveries[d_left - 1] == 0:
                d_left -= 1
            else:
                deliveries[d_left - 1] -= 1
                d -= 1
        p = cap
        while p_left and p:
            if pickups[p_left - 1] == 0:
                p_left -= 1
            else:
                pickups[p_left - 1] -= 1
                p -= 1
        while d_left:
            if deliveries[d_left - 1] == 0:
                d_left -= 1
            else:
                break
        while p_left:
            if pickups[p_left - 1] == 0:
                p_left -= 1
            else:
                break
    return answer