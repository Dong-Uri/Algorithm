from collections import deque
import copy

N, M = map(int, input().split())
sr, sc, er, ec = map(int, input().split())
A = list(map(int, input().split()))
village = []
for _ in range(N):
    village.append(list(map(int, input().split())))

queue = deque([[sr, sc, []]])
visited = copy.deepcopy(village)
visited[sr][sc] = 1
while queue:
    now = queue.popleft()
    for ai, aj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        if now[0] + ai == -1 or now[0] + ai == N or now[1] + aj == -1 or now[1] + aj == N:
            continue
        if visited[now[0] + ai][now[1] + aj]:
            continue
        visited[now[0] + ai][now[1] + aj] = 1
        route = now[2] + [[now[0] + ai, now[1] + aj]]
        if now[0] + ai == er and now[1] + aj == ec:
            break
        queue.append([now[0] + ai, now[1] + aj, route])
    if now[0] + ai == er and now[1] + aj == ec:
        break
else:
    route = []
    print(-1)

A_map = [[0] * N for _ in range(N)]
for i in range(M):
    A_map[A[2 * i]][A[2 * i + 1]] += 1

for nr, nc in route:
    # print(nr, nc)
    # print(A_map)
    if nr == er and nc == ec:
        print(0)
        break
    mv, st, at = 0, 0, 0
    A_map[nr][nc] = 0
    
    # 상
    st_u = 0
    A_map_u = [[0] * N for _ in range(N)]
    vision_u = [[0] * N for _ in range(N)]
    e = -1
    for i in range(nr - 1, -1, -1):
        ii = i
        jj = nc - 1
        while ii >= 0 and jj > e:
            vision_u[ii][jj] = 1
            if A_map[ii][jj]:
                A_map_u[ii][jj] = A_map[ii][jj]
                st_u += A_map[ii][jj]
                e = jj
                break
            ii -= 1
            jj -= 1
    e = N
    for i in range(nr - 1, -1, -1):
        ii = i
        jj = nc + 1
        while ii >= 0 and jj < e:
            vision_u[ii][jj] = 1
            if A_map[ii][jj]:
                A_map_u[ii][jj] = A_map[ii][jj]
                st_u += A_map[ii][jj]
                e = jj
                break
            ii -= 1
            jj += 1
    j = nc
    for i in range(nr - 1, -1, -1):
        vision_u[i][j] = 1
        if A_map[i][j]:
            A_map_u[i][j] = A_map[i][j]
            st_u += A_map[i][j]
            break
    if st_u > st:
        st = st_u
        A_map_next = A_map_u
        vision = vision_u

    # 하
    st_d = 0
    A_map_d = [[0] * N for _ in range(N)]
    vision_d = [[0] * N for _ in range(N)]
    e = -1
    for i in range(nr + 1, N):
        ii = i
        jj = nc - 1
        while ii < N and jj > e:
            vision_d[ii][jj] = 1
            if A_map[ii][jj]:
                A_map_d[ii][jj] = A_map[ii][jj]
                st_d += A_map[ii][jj]
                e = jj
                break
            ii += 1
            jj -= 1
    e = N
    for i in range(nr + 1, N):
        ii = i
        jj = nc + 1
        while ii < N and jj < e:
            vision_d[ii][jj] = 1
            if A_map[ii][jj]:
                A_map_d[ii][jj] = A_map[ii][jj]
                st_d += A_map[ii][jj]
                e = jj
                break
            ii += 1
            jj += 1
    j = nc
    for i in range(nr + 1, N):
        vision_d[i][j] = 1
        if A_map[i][j]:
            A_map_d[i][j] = A_map[i][j]
            st_d += A_map[i][j]
            break
    if st_d > st:
        st = st_d
        A_map_next = A_map_d
        vision = vision_d

    # 좌
    st_l = 0
    A_map_l = [[0] * N for _ in range(N)]
    vision_l = [[0] * N for _ in range(N)]
    e = -1
    for j in range(nc - 1, -1, -1):
        jj = j
        ii = nr - 1
        while jj >= 0 and ii > e:
            vision_l[ii][jj] = 1
            if A_map[ii][jj]:
                A_map_l[ii][jj] = A_map[ii][jj]
                st_l += A_map[ii][jj]
                e = ii
                break
            ii -= 1
            jj -= 1
    e = N
    for j in range(nc - 1, -1, -1):
        jj = j
        ii = nr + 1
        while jj >= 0 and ii < e:
            vision_l[ii][jj] = 1
            if A_map[ii][jj]:
                A_map_l[ii][jj] = A_map[ii][jj]
                st_l += A_map[ii][jj]
                e = ii
                break
            ii += 1
            jj -= 1
    i = nr
    for j in range(nc - 1, -1, -1):
        vision_l[i][j] = 1
        if A_map[i][j]:
            A_map_l[i][j] = A_map[i][j]
            st_l += A_map[i][j]
            break
    if st_l > st:
        st = st_l
        A_map_next = A_map_l
        vision = vision_l

    # 우
    st_r = 0
    A_map_r = [[0] * N for _ in range(N)]
    vision_r = [[0] * N for _ in range(N)]
    e = -1
    for j in range(nc + 1, N):
        jj = j
        ii = nr - 1
        while jj < N and ii > e:
            vision_r[ii][jj] = 1
            if A_map[ii][jj]:
                A_map_r[ii][jj] = A_map[ii][jj]
                st_r += A_map[ii][jj]
                e = ii
                break
            ii -= 1
            jj += 1
    e = N
    for j in range(nc + 1, N):
        jj = j
        ii = nr + 1
        while jj < N and ii < e:
            vision_r[ii][jj] = 1
            if A_map[ii][jj]:
                A_map_r[ii][jj] = A_map[ii][jj]
                st_r += A_map[ii][jj]
                e = ii
                break
            ii += 1
            jj += 1
    j = nr
    for j in range(nc + 1, N):
        vision_r[i][j] = 1
        if A_map[i][j]:
            A_map_r[i][j] = A_map[i][j]
            st_r += A_map[i][j]
            break
    if st_r > st:
        st = st_r
        A_map_next = A_map_r
        vision = vision_r

    A_map_dummy1 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A_map[i][j] and not A_map_next[i][j]:
                if i - nr > 0 and not vision[i - 1][j]:
                    mv += A_map[i][j]
                    A_map_dummy1[i - 1][j] += A_map[i][j]
                    continue
                if nr - i > 0 and not vision[i + 1][j]:
                    mv += A_map[i][j]
                    A_map_dummy1[i + 1][j] += A_map[i][j]
                    continue
                if j - nc > 0 and not vision[i][j - 1]:
                    mv += A_map[i][j]
                    A_map_dummy1[i][j - 1] += A_map[i][j]
                    continue
                if nc - j > 0 and not vision[i][j + 1]:
                    mv += A_map[i][j]
                    A_map_dummy1[i][j + 1] += A_map[i][j]
                    continue
                A_map_dummy1[i][j] += A_map[i][j]

    A_map_dummy2 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A_map_dummy1[i][j] and not A_map_next[i][j]:
                if j - nc > 0 and not vision[i][j - 1]:
                    mv += A_map_dummy1[i][j]
                    A_map_dummy2[i][j - 1] += A_map_dummy1[i][j]
                    continue
                if nc - j > 0 and not vision[i][j + 1]:
                    mv += A_map_dummy1[i][j]
                    A_map_dummy2[i][j + 1] += A_map_dummy1[i][j]
                    continue
                if i - nr > 0 and not vision[i - 1][j]:
                    mv += A_map_dummy1[i][j]
                    A_map_dummy2[i - 1][j] += A_map_dummy1[i][j]
                    continue
                if nr - i > 0 and not vision[i + 1][j]:
                    mv += A_map_dummy1[i][j]
                    A_map_dummy2[i + 1][j] += A_map_dummy1[i][j]
                    continue
                A_map_dummy2[i][j] += A_map_dummy1[i][j]

    for i in range(N):
        for j in range(N):
            A_map_next[i][j] += A_map_dummy2[i][j]
    # print(A_map_dummy1)
    # print(A_map_dummy2)
    # print(A_map_next)
    # print(vision)
    at += A_map_next[nr][nc]
    A_map_next[nr][nc] = 0
    A_map = A_map_next
    print(mv, st, at)