info = [[] for _ in range(13)]
for _ in range(3):
    chk = list(input().split())
    if not chk:
        chk = list(input().split())
    left = list(map(int, chk[:4]))
    right = list(map(int, chk[5:]))
    if chk[4] == '<':
        for i in range(1, 13):
            if i in left:
                info[i].append('-')
            elif i in right:
                info[i].append('+')
            else:
                info[i].append('=')
    elif chk[4] == '>':
        for i in range(1, 13):
            if i in left:
                info[i].append('+')
            elif i in right:
                info[i].append('-')
            else:
                info[i].append('=')
    else:
        for i in range(1, 13):
            if i in left or i in right:
                info[i].append('=')
            else:
                info[i].append('?')

ans = []
for i in range(1, 13):
    if '=' in info[i]:
        pass
    elif '+' in info[i] and '-' in info[i]:
        pass
    else:
        ans.append(i)

if len(ans) == 0:
    print('impossible')
elif len(ans) > 1:
    print('indefinite')
else:
    ans = ans[0]
    if '+' in info[ans]:
        print(str(ans) + '+')
    elif '-' in info[ans]:
        print(str(ans) + '-')
    else:
        print('indefinite')