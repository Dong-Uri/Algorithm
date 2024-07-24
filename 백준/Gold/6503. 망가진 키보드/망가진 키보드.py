import sys
input = sys.stdin.readline

while True:
    m = int(input())
    if not m:
        break
    stc = input().rstrip()
    stc_l = len(stc)
    if stc_l < m:
        print(stc_l)
        continue
    ans = 1
    l = 0
    r = 1
    chr_dict = {stc[0] : 1}
    chr_n = 1
    while r < stc_l:
        if chr_n <= m:
            if r - l > ans:
                ans = r - l
            if stc[r] in chr_dict.keys():
                chr_dict[stc[r]] += 1
                if chr_dict[stc[r]] == 1:
                    chr_n += 1
            else:
                chr_dict[stc[r]] = 1
                chr_n += 1
            r += 1
        else:
            chr_dict[stc[l]] -= 1
            if chr_dict[stc[l]] == 0:
                chr_n -= 1
            l += 1
    if chr_n <= m:
        if r - l > ans:
            ans = r - l
    print(ans)