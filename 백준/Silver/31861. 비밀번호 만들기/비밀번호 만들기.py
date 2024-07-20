N, M = map(int, input().split())
pwds = [1] * 26
for _ in range(M - 1):
    pwd_sum = sum(pwds) % 1000000007
    new_pwds = [pwd_sum] * 26
    for i in range(26):
        new_pwds[i] -= sum(pwds[max(0, i - N + 1):min(26, i + N)])
    pwds = new_pwds
print(sum(pwds) % 1000000007)