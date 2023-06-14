import sys

r, c = map(int, sys.stdin.readline().split())  # 그래프 크기 (90도 회전했다고 가정 후 입력)
k = int(sys.stdin.readline())  # 대기번호
if k > (c * r) :  # 불가능
    print(0)
    exit()

graph = [[0] * c for _ in range(r)]
dx = [0, 1, 0, -1]  # 시계방향 : 동->남->서->북
dy = [1, 0, -1, 0]
dir = 0  # 기본방향
now = [0, -1]   # 배정할 위치
res = 0  # 대기번호

while res < k:
    res += 1
    # print(res, now)
    while True:
        nx = now[0] + dx[dir]  # 다음위치
        ny = now[1] + dy[dir]
        if nx in range(r) and ny in range(c):  # 범위 포함
            if graph[nx][ny] == 0:
                graph[nx][ny] = res
                now = [nx, ny]  # 위치 갱신
                break
            else:
                dir = (dir + 1) % 4
        else:  # 범위 이탈 -> 시계방향 전환
            dir = (dir + 1) % 4
print(now[0]+1, now[1]+1)