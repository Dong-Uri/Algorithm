def make_choco(n):
    if n == 0:
        return []
    if n == 2:
        return ['R', 'RR']
    if n % 12 == 0 or n % 12 == 2:
        choco = make_choco(n - 3)
        choco.append('B' * (n - 2))
        choco.append('RB' * (n // 2 - 1) + 'R')
        choco.append('R' * n)
        return choco
    if n % 12 == 9 or n % 12 == 11:
        choco = make_choco(n - 9)
        new_choco = ['R', 'RR']
        for _ in range((n - 5) // 2):
            new_choco.append('RBB')
            new_choco.append('RRB')
        new_choco[3] += 'R'
        new_choco[4] += 'RR'
        new_choco[5] += 'BBR'
        for i in range((n - 9) // 2):
            new_choco[6 + i * 2] += choco[i * 2] + 'BRR'
            new_choco[7 + i * 2] += choco[i * 2 + 1] + 'BBR'
        new_choco.append('B' * (n - 4) + 'RR')
        new_choco.append('RB' * ((n - 2) // 2) + 'BR')
        new_choco.append('R' * (n - 3) + 'BRR')
        return new_choco

N = int(input())
choco = make_choco(N)
for c in choco:
    print(c)