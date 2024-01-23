def solution(numbers):
    
    def split(n):
        m_point = (len(n) + 1) // 2 - 1
        m = n[m_point]
        l = n[:m_point]
        r = n[m_point + 1:]
        return m, l, r
    
    def is_tree(n):
        nonlocal ans
        if not ans:
            return
        if len(n) == 1:
            return
        m, l, r = split(n)
        if m == '0':
            if '1' in l or '1' in r:
                ans = 0
                return
        else:
            is_tree(l)
            is_tree(r)
        return        
    
    answer = []
    for number in numbers:
        b_num = bin(number)[2:]
        length = 1
        while True:
            if len(b_num) >= length and len(b_num) < length * 2:
                b_num = '0' * (length * 2 - len(b_num) - 1) + b_num
                break
            length *= 2
        ans = 1
        is_tree(b_num)
        answer.append(ans)
    return answer