def are_same(a, b, c, d, x, y, z, w):
    if a == x:
        if b == y:
            if c == z:
                if d == w:
                    return 1
        if c == y:
            if d == z:
                if b == w:
                    return 1
        if d == y:
            if b == z:
                if c == w:
                    return 1
    if b == x:
        if d == y:
            if c == z:
                if a == w:
                    return 1
        if c == y:
            if a == z:
                if d == w:
                    return 1
        if a == y:
            if d == z:
                if c == w:
                    return 1
    if c == x:
        if b == y:
            if d == z:
                if a == w:
                    return 1
        if d == y:
            if a == z:
                if b == w:
                    return 1
        if a == y:
            if b == z:
                if d == w:
                    return 1
    if d == x:
        if c == y:
            if b == z:
                if a == w:
                    return 1
        if b == y:
            if a == z:
                if c == w:
                    return 1
        if a == y:
            if c == z:
                if b == w:
                    return 1
    return 0

K = int(input())
for _ in range(K):
    a, b, c, d, x, y, z, w = map(int, input().split())
    print(are_same(a, b, c, d, x, y, z, w))