import sys
input = sys.stdin.readline

def turn(A, way):
    if way == 0:
        temp = A[0][0]
        A[0][0] = A[2][0]
        A[2][0] = A[2][2]
        A[2][2] = A[0][2]
        A[0][2] = temp
        temp = A[0][1]
        A[0][1] = A[1][0]
        A[1][0] = A[2][1]
        A[2][1] = A[1][2]
        A[1][2] = temp
    if way == 1:
        temp = A[0][0]
        A[0][0] = A[0][2]
        A[0][2] = A[2][2]
        A[2][2] = A[2][0]
        A[2][0] = temp
        temp = A[1][0]
        A[1][0] = A[0][1]
        A[0][1] = A[1][2]
        A[1][2] = A[2][1]
        A[2][1] = temp
    return A

def side(A, side, way, temp1, temp2, temp3):
    if side == 0:
        if way == 0:
            new_temp1 = A[0][0]
            new_temp2 = A[0][1]
            new_temp3 = A[0][2]
            A[0][0] = temp1
            A[0][1] = temp2
            A[0][2] = temp3
        if way == 1:
            new_temp1 = A[0][2]
            new_temp2 = A[0][1]
            new_temp3 = A[0][0]
            A[0][2] = temp1
            A[0][1] = temp2
            A[0][0] = temp3
    if side == 1:
        if way == 0:
            new_temp1 = A[0][2]
            new_temp2 = A[1][2]
            new_temp3 = A[2][2]
            A[0][2] = temp1
            A[1][2] = temp2
            A[2][2] = temp3
        if way == 1:
            new_temp1 = A[2][2]
            new_temp2 = A[1][2]
            new_temp3 = A[0][2]
            A[2][2] = temp1
            A[1][2] = temp2
            A[0][2] = temp3
    if side == 2:
        if way == 0:
            new_temp1 = A[2][0]
            new_temp2 = A[2][1]
            new_temp3 = A[2][2]
            A[2][0] = temp1
            A[2][1] = temp2
            A[2][2] = temp3
        if way == 1:
            new_temp1 = A[2][2]
            new_temp2 = A[2][1]
            new_temp3 = A[2][0]
            A[2][2] = temp1
            A[2][1] = temp2
            A[2][0] = temp3
    if side == 3:
        if way == 0:
            new_temp1 = A[0][0]
            new_temp2 = A[1][0]
            new_temp3 = A[2][0]
            A[0][0] = temp1
            A[1][0] = temp2
            A[2][0] = temp3
        if way == 1:
            new_temp1 = A[2][0]
            new_temp2 = A[1][0]
            new_temp3 = A[0][0]
            A[2][0] = temp1
            A[1][0] = temp2
            A[0][0] = temp3
    return A, new_temp1, new_temp2, new_temp3

def turn_side(X, side1, way1, Y, side2, way2, Z, side3, way3, W, side4, way4):
    X, temp1, temp2, temp3 = side(X, side1, way1, 't', 't', 't')
    Y, temp1, temp2, temp3 = side(Y, side2, way2, temp1, temp2, temp3)
    Z, temp1, temp2, temp3 = side(Z, side3, way3, temp1, temp2, temp3)
    W, temp1, temp2, temp3 = side(W, side4, way4, temp1, temp2, temp3)
    X, _, _, _ = side(X, side1, way1, temp1, temp2, temp3)
    return X, Y, Z, W

T = int(input())
for _ in range(T):
    U = [['w'] * 3 for _ in range(3)]
    D = [['y'] * 3 for _ in range(3)]
    F = [['r'] * 3 for _ in range(3)]
    B = [['o'] * 3 for _ in range(3)]
    L = [['g'] * 3 for _ in range(3)]
    R = [['b'] * 3 for _ in range(3)]
    
    n = int(input())
    turn_list = input().split()
    for t in turn_list:
        if t[1] == '+':
            way = 0
        if t[1] == '-':
            way = 1
        if t[0] == 'U':
            U = turn(U, way)
            if way == 0:
                F, L, B, R = turn_side(F, 0, 1, L, 0, 1, B, 0, 1, R, 0, 1)
            if way == 1:
                F, R, B, L = turn_side(F, 0, 0, R, 0, 0, B, 0, 0, L, 0, 0)
        if t[0] == 'D':
            D = turn(D, way)
            if way == 0:
                F, R, B, L = turn_side(F, 2, 0, R, 2, 0, B, 2, 0, L, 2, 0)
            if way == 1:
                F, L, B, R = turn_side(F, 2, 1, L, 2, 1, B, 2, 1, R, 2, 1)
        if t[0] == 'F':
            F = turn(F, way)
            if way == 0:
                U, R, D, L = turn_side(U, 2, 0, R, 3, 0, D, 2, 0, L, 1, 1)
            if way == 1:
                U, L, D, R = turn_side(U, 2, 1, L, 1, 0, D, 2, 1, R, 3, 1)
        if t[0] == 'B':
            B = turn(B, way)
            if way == 0:
                U, L, D, R = turn_side(U, 0, 1, L, 3, 0, D, 0, 1, R, 1, 1)
            if way == 1:
                U, R, D, L = turn_side(U, 0, 0, R, 1, 0, D, 0, 0, L, 3, 1)
        if t[0] == 'L':
            L = turn(L, way)
            if way == 0:
                U, F, D, B = turn_side(U, 3, 0, F, 3, 0, D, 1, 1, B, 1, 1)
            if way == 1:
                U, B, D, F = turn_side(U, 3, 1, B, 1, 0, D, 1, 0, F, 3, 1)
        if t[0] == 'R':
            R = turn(R, way)
            if way == 0:
                U, B, D, F = turn_side(U, 1, 1, B, 3, 0, D, 3, 0, F, 1, 1)
            if way == 1:
                U, F, D, B = turn_side(U, 1, 0, F, 1, 0, D, 3, 1, B, 3, 1)
    for u in U:
        print(''.join(u))
