def solution(n):
    che = [True] * (10 ** 6 + 1)
    che[0] = False
    che[1] = False
    ans = 0
    for i in range(n + 1):
        if che[i]:
            ans += 1
            j = 2
            while i * j <= 10 ** 6:
                che[i * j] = False
                j += 1
    return ans