def solution(diffs, times, limit):
    l = 0
    r = max(diffs) + 1
    while l + 1 < r:
        level = (l + r) // 2
        solved = True
        time = 0
        time_prev = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            if diff <= level:
                time += time_cur
            else:
                wrong = diff - level
                time += time_cur * (wrong + 1) + time_prev * wrong
            time_prev = time_cur
            if time > limit:
                solved = False
                break
        if solved:
            r = level
        else:
            l = level
    answer = r
    return answer