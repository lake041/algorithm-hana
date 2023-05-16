# 토마토
# https://www.acmicpc.net/problem/7576
# bfs 조금 지저분한 듯

from collections import deque
from sys import stdin
input = stdin.readline

M, N = map(int, input().split())
bod = [list(map(int, input().split())) for _ in range(N)]
q = deque()
cnt = 0
rot = 0
day = 0

init = []
for y in range(N):
    for x in range(M):
        if bod[y][x] == 1:
            cnt += 1
            q.append([y, x])
        if bod[y][x] == -1:
            rot += 1
if cnt == N*M-rot:
    print(day)
    exit()

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

t = len(q)
while q:
    while t > 0:
        y, x = q.popleft()
        t -= 1
        for k in range(4):
            ny, nx = y+dy[k], x+dx[k]
            if 0<=ny<=N-1 and 0<=nx<=M-1 and bod[ny][nx]==0:
                cnt += 1
                bod[ny][nx] = 1
                q.append([ny, nx])
    if cnt == N*M-rot:
        break
    t = len(q)
    day += 1

if cnt == N*M-rot:
    print(day+1)
else:
    print(-1)