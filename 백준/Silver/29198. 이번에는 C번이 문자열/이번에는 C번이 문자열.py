import copy

N, M, K = map(int, input().split())
cnt_lst = [0] * 26
char_lst = []
for _ in range(N):
    char_cnt = copy.deepcopy(cnt_lst)
    char = input()
    for c in char:
        char_cnt[ord(c) - 65] -= 1
    char_lst.append(char_cnt)
char_lst.sort()
for i in range(K):
    for j in range(26):
        cnt_lst[j] -= char_lst[i][j]
ans = ''
for i in range(26):
    for _ in range(cnt_lst[i]):
        ans += chr(i + 65)
print(ans)