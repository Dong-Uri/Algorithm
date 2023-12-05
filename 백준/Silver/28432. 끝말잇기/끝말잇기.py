N = int(input())
words = []
for _ in range(N):
    words.append(input())
i = words.index('?')
if i == 0:
    before = False
else:
    before = words[i-1][-1]
if i == N-1:
    after = False
else:
    after = words[i+1][0]

M = int(input())
for _ in range(M):
    word = input()
    if not before or word[0] == before:
        if not after or word[-1] == after:
            if word not in words:
                print(word)
                break