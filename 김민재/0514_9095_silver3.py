# 1, 2, 3 더하기
# https://www.acmicpc.net/problem/9095
# DP

from sys import stdin
input = stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    f = [0]*(n+1)
    for i in range(1, n+1):
        if i == 1:
            f[i] = 1
        elif i == 2:
            f[i] = 2
        elif i == 3:
            f[i] = 4
        else:
            f[i] = f[i-1] + f[i-2] + f[i-3]
    print(f[n])