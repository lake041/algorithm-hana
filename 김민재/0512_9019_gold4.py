# DSLR
# https://www.acmicpc.net/problem/9019
# bfs
# 큐에 D S L R 함수별로 4번씩 append 하는 게 멋이 안 나서 함수로 한번에 묶어서 집어넣었더니 시간 초과 남
# 그냥 무식하게 코드를 네번 복붙해서 넣었더니 통과됨 why? 재귀 때문에 그런가
# pypy로 제출해야만 통과되는 걸 보면 일단 좋은 문제는 아닌 듯

from collections import deque
from sys import stdin
input = stdin.readline

def D(num):
    return (num*2)%10000
def S(num):
    return (num-1)%10000
def L(num):
    return (num*10+num//1000)%10000
def R(num):
    return ((num%10)*1000+num//10)%10000

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [False]*10000
    visited[A] = True
    q = deque()
    q.append([A, ''])
    while q:
        i, j = q.popleft()
        if i == B:
            print(j)
            break
        
        nxt = D(i)
        if not visited[nxt]:
            visited[nxt] = True
            q.append([nxt, j+'D'])

        nxt = S(i)
        if not visited[nxt]:
            visited[nxt] = True
            q.append([nxt, j+'S'])

        nxt = L(i)
        if not visited[nxt]:
            visited[nxt] = True
            q.append([nxt, j+'L'])

        nxt = R(i)
        if not visited[nxt]:
            visited[nxt] = True
            q.append([nxt, j+'R'])
