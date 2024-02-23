def solution(n, k, cmd):
    answer = ''
    table = [[True, i - 1, i + 1] for i in range(n)]
    stack = []
    for c in cmd:
        if c[0] == 'D':
            m = int(c[2:])
            while m:
                k = table[k][2]
                m -= 1
        if c[0] == 'U':
            m = int(c[2:])
            while m:
                k = table[k][1]
                m -= 1
        if c == 'C':
            stack.append(k)
            table[k][0] = False
            a = table[k][1]
            b = table[k][2]
            if a != -1:
                table[a][2] = b
            if b != n:
                table[b][1] = a
            k = b
            if k == n:
                k = a
        if c == "Z":
            l = stack.pop()
            table[l][0] = True
            a = table[l][1]
            b = table[l][2]
            if a != -1:
                table[a][2] = l
            if b != n:
                table[b][1] = l          
            
    for t in table:
        if t[0]:
            answer += 'O'
        else:
            answer += 'X'
            
    return answer