# 뱀의 위치를 Queue에 넣는 생각...!

from collections import deque

N = int(input())
K = int(input())

board = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(K):
    y, x = map(int, input().split())
    board[y - 1][x - 1] = 1

L = int(input())
dirDict = dict()
queue = deque([[0, 0]])

for i in range(L):
    r, c = input().split()
    dirDict[int(r)] = c

x, y = 0, 0
board[y][x] = 2
cnt = 0
direction = 0

def rotate(c):
    global direction
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4


while True:
    cnt += 1
    x += dx[direction]
    y += dy[direction]

    if x < 0 or x >= N or y < 0 or y >= N:
        break

    if board[y][x] == 1:
        board[y][x] = 2
        queue.append((x, y))
        if cnt in dirDict:
            rotate(dirDict[cnt])

    elif board[y][x] == 0:
        board[y][x] = 2
        queue.append((x, y))
        tx, ty = queue.popleft()
        board[ty][tx] = 0
        if cnt in dirDict:
            rotate(dirDict[cnt])

    else:
        break

print(cnt)
