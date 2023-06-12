import sys
from collections import deque

snake = deque()
dx = [0, 1, 0, -1]  # 동, 남, 서, 북
dy = [1, 0, -1, 0]
n = int(sys.stdin.readline())
graph = [[0] * n for _ in range(n)]
k = int(sys.stdin.readline())  # 사과 개수
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    graph[r-1][c-1] = 1  # 사과
l = int(sys.stdin.readline())  # 방향전환횟수
change = dict()
for _ in range(l):
    a, b = ''.join(sys.stdin.readline().rstrip()).split()
    change[int(a)] = b  # 시기, 방향 입력

cnt = 0
dir = 0
snake.append([0, 0])
while True:
    cnt += 1
    head_x, head_y = snake[0][0] + dx[dir], snake[0][1] + dy[dir]  # 몸 길이를 늘림(머리)
    if head_x in range(n) and head_y in range(n):  # 벽과 충돌 여부 파악
        if [head_x, head_y] in snake:  # 본인 몸과 충돌
            print(cnt)
            break
        snake.appendleft([head_x, head_y])  # 머리 이동
        if graph[head_x][head_y] == 1:  # 사과 발견
            graph[head_x][head_y] = 0  # 먹음처리
            # continue -> 이거 있어서 오답
        else:  # 사과 없으면
            snake.pop()  # 축소(꼬리 삭제)
    else:  # 벽과 충돌
        print(cnt)
        break
    # 방향전환
    if cnt in change:  # 전환할 것이 있고, n초 경과
        turn = change[cnt]
        if turn == "D":  # 오른쪽 90도 회전
            dir = (dir + 1) % 4
        elif turn == "L":  # 왼쪽 90도 회전
            dir -= 1
            if dir < 0: dir = 3
    print(snake)