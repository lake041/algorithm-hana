# 쿼드트리
# https://www.acmicpc.net/problem/1992
# 분할정복, 인터넷 풀이 거의 복사해왔다.
# 당장 이해는 했지만 계속 비슷한 유형 복습하면서 익혀봐야지.

from sys import stdin
input = stdin.readline

N = int(input())
bod = [list(map(int, list(input().rstrip()))) for _ in range(N)]

def cut(y, x, size):
    init = bod[y][x]
    for i in range(y, y + size):
        for j in range(x, x + size):
            if bod[i][j] != init:
                print("(", end='')
                nxt_size = size//2
                cut(y, x, nxt_size)
                cut(y, x+nxt_size, nxt_size)
                cut(y+nxt_size, x, nxt_size)
                cut(y+nxt_size, x+nxt_size, nxt_size)
                print(")", end='')
                return
    print(init, end="")

cut(0, 0, N)
