# 유기농 배추
# https://www.acmicpc.net/problem/1012
# greedy
# 

from sys import stdin
from collections import deque
from itertools import product
input = stdin.readline

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    bod = [[0]*M for _ in range(N)]
    check = [[0]*M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        bod[Y][X] = 1
    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    cnt = 0
    q = deque()
    for i, j in product(range(M), range(N)):
        if bod[j][i]==0 or check[j][i]==1:
            continue
        check[j][i] = 1
        cnt += 1
        print(j, i, cnt)
        q.append((i, j))
        while q:
            x, y = q.popleft()
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0<=nx<=M-1 and 0<=ny<=N-1 and bod[ny][nx]==1 and check[ny][nx]==0:
                    check[ny][nx] = 1
                    q.append((ny, nx))
    print(cnt)