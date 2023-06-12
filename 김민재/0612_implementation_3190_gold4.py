# 뱀
# https://www.acmicpc.net/problem/3190
# implementation
#

from sys import stdin
from collections import deque
input = stdin.readline

# 0: 빈 땅
N = int(input())
bod = [[0 for _ in range(N)] for _ in range(N)]

# 1: 사과
K = int(input())
for _ in range(K):
    y, x = map(int, input().split())
    bod[y-1][x-1] = 1

# 방향 전환
L = int(input())
transitions = deque()
for _ in range(L):
    X, C = input().split()
    transitions.append([int(X), C])

#     북  동  남  서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def transition(prev_direction_index, char):
    if char == 'L':
        return (prev_direction_index-1) % 4
    if char == 'D':
        return (prev_direction_index+1) % 4


def move(snake_body, snake_direction):
    head = snake_body[-1]
    y, x = head

    # 한 칸 move
    y += dy[snake_direction]
    x += dx[snake_direction]
    if [y, x] in snake_body or not (0 <= y < N and 0 <= x < N):
        return 'yes'
    snake_body.append([y, x])

    # 사과 냠냠?
    if bod[y][x] == 1:
        bod[y][x] = 0
    else:
        snake_body.popleft()
    return 'no'


snake_body = deque([[0, 0]])
snake_direction = 1
time = 0

while True:
    is_done = move(snake_body, snake_direction)
    time += 1

    if transitions:
        X, C = transitions[0]
        if X == time:
            snake_direction = transition(snake_direction, C)
            transitions.popleft()

    if is_done == 'yes':
        print(time)
        break
