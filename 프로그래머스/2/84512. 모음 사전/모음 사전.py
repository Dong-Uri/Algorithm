def solution(word):
    dic = ['']
    moum = ['A', 'E', 'I', 'O', 'U']
    add = ['']
    for _ in range(5):
        new_add = []
        for a in add:
            for m in moum:
                new_add.append(a + m)
        add = new_add
        dic += add
    dic.sort()
    return dic.index(word)