from sys import setrecursionlimit
from sys import stdin
input = stdin.readline
setrecursionlimit(10000)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    bod = [[0]*M for _ in range(N)]
    check = [[False]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        bod[y][x] = 1

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    def dfs(y, x):
        check[y][x] = True
        for u, v in zip(dy, dx):
            ny, nx = y+u, x+v
            if 0<=ny<=N-1 and 0<=nx<=M-1 and bod[ny][nx]==1 and check[ny][nx]==False:
                dfs(ny, nx)

    ans = 0
    for y in range(N):
        for x in range(M):
            if bod[y][x]==1 and check[y][x]==False:
                dfs(y, x)
                ans += 1
    print(ans)