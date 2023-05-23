# 적록색약
# https://www.acmicpc.net/problem/10026
# bfs, 함수 복붙한 게 자랑

from collections import deque
from itertools import product
from sys import stdin
input = stdin.readline

N = int(input())
bod = [list(input().rstrip()) for _ in range(N)]
q = deque()
visited = [[False]*N for _ in range(N)]
ans1, ans2 = 0, 0

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i, j in product(range(N), repeat=2):
    if visited[i][j] == True:
        continue
    visited[i][j] = True
    q.append([i, j])
    ans1 += 1
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0<=ny<N and 0<=nx<N and visited[ny][nx]==False and bod[ny][nx]==bod[y][x]:
                visited[ny][nx] = True
                q.append([ny, nx])

for i, j in product(range(N), repeat=2):
    if bod[i][j] == 'G':
        bod[i][j] = 'R'
visited = [[False]*N for _ in range(N)]

q = deque()
for i, j in product(range(N), repeat=2):
    if visited[i][j] == True:
        continue
    visited[i][j] = True
    q.append([i, j])
    ans2 += 1
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0<=ny<N and 0<=nx<N and visited[ny][nx]==False and bod[ny][nx]==bod[y][x]:
                visited[ny][nx] = True
                q.append([ny, nx])

print(ans1, ans2)