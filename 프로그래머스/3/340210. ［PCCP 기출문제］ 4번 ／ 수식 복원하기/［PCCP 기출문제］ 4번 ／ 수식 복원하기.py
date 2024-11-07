def solution(expressions):
    def jb_change(str_n, a, b):
        if str_n == '0':
            return '0'
        if a == 10:
            n = int(str_n)
            m = ''
            while n:
                m = str(n % b) + m
                n //= b
            return m
        if b == 10:
            m = 0
            for i in range(len(str_n)):
                m += int(str_n[i]) * (a ** (len(str_n) - i - 1))
            return str(m)
    knowns = []
    unknowns = []
    max_n = 1
    for expression in expressions:
        for str_n in ['2', '3', '4', '5', '6', '7', '8']:
            if str_n in expression and int(str_n) > max_n:
                max_n = int(str_n)
        if 'X' in expression:
            unknowns.append(expression)
        else:
            knowns.append(expression)
    possible = []
    for n in range(max_n + 1, 10):
        possible.append(n)
    knowns_10 = []
    for known in knowns:
        A, S, B, _, C = known.split()
        if S == '+':
            knowns_10.append([A, B, C])
        else:
            knowns_10.append([B, C, A])
    jbs = []
    for p in possible:
        for A, B, C in knowns_10:
            if C != jb_change(str(int(jb_change(A, p, 10)) + int(jb_change(B, p, 10))), 10, p):
                break
        else:
            jbs.append(p)
    answer = []
    for unknown in unknowns:
        A, S, B, _, _ = unknown.split()
        ans_list = set()
        for p in jbs:
            if S == '+':
                ans_list.add(jb_change(str(int(jb_change(A, p, 10)) + int(jb_change(B, p, 10))), 10, p))
            else:
                ans_list.add(jb_change(str(int(jb_change(A, p, 10)) - int(jb_change(B, p, 10))), 10, p))
            if len(ans_list) == 2:
                break
        if len(ans_list) == 2:
            answer.append(unknown[:-1] + '?')
        else:
            ans = ans_list.pop()
            answer.append(unknown[:-1] + ans)
    return answer