T = int(input())
for _ in range(T):
    S = input()
    word_dict = dict()
    for i in range(65, 91):
        word_dict[chr(i)] = True
    for s in S:
        word_dict[s] = False
    ans = 0
    for s, TF in word_dict.items():
        if TF:
            ans += ord(s)
    print(ans)