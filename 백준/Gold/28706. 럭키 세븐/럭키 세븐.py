import sys

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    TF = [False] * 7
    TF[1] = True
    for _ in range(N):
        new_TF = [False] * 7
        choice = list(sys.stdin.readline().rstrip().split())
        for i in range(7):
            if TF[i]:
                n = int(choice[1])
                if choice[0] == '+':
                    new_TF[(i + n) % 7] = True
                else:
                    new_TF[(i * n) % 7] = True
                n = int(choice[3])
                if choice[2] == '+':
                    new_TF[(i + n) % 7] = True
                else:
                    new_TF[(i * n) % 7] = True
        TF = new_TF
    if TF[0]:
        print('LUCKY')
    else:
        print('UNLUCKY')