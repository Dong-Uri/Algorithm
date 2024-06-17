N = int(input())
tang = list(map(int, input().split()))
if N < 3:
    print(N)
else:
    ans = 2
    l = 0
    r = 3
    frt_cnt = [0] * 10
    frt_cnt[tang[0]] += 1
    frt_cnt[tang[1]] += 1
    frt_cnt[tang[2]] += 1
    while True:
        if r == N:
            if r - l > ans:
                if frt_cnt.count(0) >= 8:
                    ans = r - l
                    break
                frt_cnt[tang[l]] -= 1
                l += 1
            else:
                break
        else:
            if frt_cnt.count(0) >= 8:
                if r - l > ans:
                    ans = r - l
                frt_cnt[tang[r]] += 1
                r += 1
            else:
                frt_cnt[tang[l]] -= 1
                l += 1
    print(ans)
