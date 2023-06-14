C, R = map(int, input().split())
K = int(input())
board = [[0 for i in range(C)] for i in range(R)]

if K > R*C:
    print(0)
else:
    cnt = 1
    direction = 0
    dx = [-1, 0, 1, 0]  # 상우하좌
    dy = [0, 1, 0, -1]

    cr = R-1
    cc = 0
    while cnt < K:
        board[cr][cc] = cnt
        nr = cr+dx[direction]
        nc = cc+dy[direction]
        if nr < 0 or nc < 0 or nr >= R or nc >= C or board[nr][nc] != 0:
            direction = (direction+1) % 4  # 방향전환
            nr = cr + dx[direction]
            nc = cc + dy[direction]

        cr = nr
        cc = nc
        cnt += 1
    print((cc+1), (R-cr))

"""
C, R = map(int, input().split())
K = int(input())

cnt = 1
x = 0
y = 0
depth = 0
board = [[0 for _ in range(C)] for _ in range(R)]


if K > C*R:
    print(0)
else:
    while cnt < K-1:
        if board[y][x] == 0:
            cnt += 1
            board[y][x] = cnt
            if y < R-1-depth and x==depth:
                y+=1
            elif y == R-1-depth and x < C-1-depth:
                x+=1
            elif y>depth and x == C-1-depth:
                y-=1
            elif y==depth and x >depth:
                x-=1
        else:
            depth+=1
            x=depth
            y=depth

    print(x+1, y+1)
"""
