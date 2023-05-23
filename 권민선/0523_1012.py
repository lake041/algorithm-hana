import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dfs(x, y):
    q = deque([(x, y)])
    board[x][y] = 0
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < M and nx >= 0 and ny < N and ny >= 0:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx, ny))

T = int(input())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    board = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        board[x][y] = 1

    answer = 0
    for i in range(M):
        for j in range(N):
            if board[i][j] == 1:
                answer += 1
                dfs(i, j)

    print(answer)