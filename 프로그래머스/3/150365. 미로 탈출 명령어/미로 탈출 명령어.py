def solution(n, m, x, y, r, c, k):
    answer = ''
    short = {'d':0, 'l':0, 'r':0, 'u':0}
    move = k
    if x < r:
        short['d'] += r - x
        move -= r - x
    if y > c:
        short['l'] += y - c
        move -= y - c
    if y < c:
        short['r'] += c - y
        move -= c - y
    if x > r:
        short['u'] += x - r
        move -= x - r
    if move < 0 or move % 2:
        return 'impossible'
    now = [x, y]
    while move:
        if short['d']:
            answer += 'd'
            now[0] += 1
            short['d'] -= 1
        elif short['l']:
            if now[0] != n:
                answer += 'd'
                now[0] += 1
                short['u'] += 1
                move -= 2
            else:
                answer += 'l'
                now[1] -= 1
                short['l'] -= 1
        elif short['r']:
            if now[0] != n:
                answer += 'd'
                now[0] += 1
                short['u'] += 1
                move -= 2
            elif now[1] != 1:
                answer += 'l'
                now[1] -= 1
                short['r'] += 1
                move -= 2
            else:
                answer += 'r'
                now[1] += 1
                short['r'] -= 1
        elif short['u']:
            if now[0] != n:
                answer += 'd'
                now[0] += 1
                short['u'] += 1
                move -= 2
            elif now[1] != 1:
                answer += 'l'
                now[1] -= 1
                short['r'] += 1
                move -= 2
            elif now[1] != m:
                answer += 'r'
                now[1] += 1
                short['l'] += 1
                move -= 2
            else:
                answer += 'u'
                now[0] -= 1
                short['u'] -= 1
        else:
            if now[0] != n:
                answer += 'd'
                now[0] += 1
                short['u'] += 1
                move -= 2
            elif now[1] != 1:
                answer += 'l'
                now[1] -= 1
                short['r'] += 1
                move -= 2
            elif now[1] != m:
                answer += 'r'
                now[1] += 1
                short['l'] += 1
                move -= 2
            elif now[0] != 1:
                answer += 'u'
                now[0] -= 1
                short['d'] += 1
                move -= 2
    answer += 'd' * short['d'] + 'l' * short['l'] + 'r' * short['r'] + 'u' * short['u']
    return answer