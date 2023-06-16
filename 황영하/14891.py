import sys
from collections import deque

def turn(now, dir, goto):  # 기준 노드, 회전방향, 진행방향(-1 : 좌 / 0 : 기준 / 1 : 우)
    # 좌 , 우 회전여부 체크
    if goto in (0, -1) and now > 0:  # 기존 왼쪽으로 진행, 범위 포함
        if gear[now - 1][2] != gear[now][6]:  # 서로 극이 다름 => 회전 가능
            turn(now-1, dir * (-1), -1)  # 왼쪽으로 진행(회전 방향은 반대로)
    if goto in (0, 1) and now < 3:  # 기존 오른쪽으로 진행, 범위 포함
        if gear[now + 1][6] != gear[now][2]:  # 서로 극이 다름 => 회전 가능
            turn(now+1, dir * (-1), 1)  # 오른쪽으로 진행
    # 회전
    if dir == 1: # 시계방향 회전
        t = gear[now].pop()
        gear[now].appendleft(t)
    elif dir == -1:  # 반시계방향 회전
        t = gear[now].popleft()
        gear[now].append(t)
    return


gear = list()
for _ in range(4):
    a = ' '.join(sys.stdin.readline().rstrip()).split()
    tmp = deque()  # 톱니바퀴 하나 -> 데크로 지정
    for i in a:
        tmp.append(i)
    gear.append(tmp)  # 톱니바퀴 입력
# for i in gear: print(i)

k = int(sys.stdin.readline())  # 회전 횟수
for _ in range(k):
    idx, dir = map(int, sys.stdin.readline().split())  # 회전시킨 톱니바퀴 번호
    turn(idx-1, dir, 0)
    # for i in gear:
    #     print(i)

res = 0
for i in range(4):
    if gear[i][0] == '1':
        res += (2 ** i)
print(res)