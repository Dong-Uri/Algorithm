import sys
input = sys.stdin.readline

N, M = map(int, input().split())
code_list = []
for _ in range(N):
    word = set(input().rstrip())
    w_code = 0
    for w in word:
        w_code += 1 << ord(w) - 97
    code_list.append(w_code)
char_list = 0
for _ in range(M):
    o, x = input().split()
    if o == '1':
        char_list += 1 << ord(x) - 97
    else:
        char_list -= 1 << ord(x) - 97
    ans = 0
    for code in code_list:
        if not code & char_list:
            ans += 1
    print(ans)