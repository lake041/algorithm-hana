# 나는야 포켓몬 마스터 이다솜
# https://www.acmicpc.net/problem/1620
# 딕셔너리 남발

from collections import defaultdict
from sys import stdin
input = stdin.readline

N, M = map(int,input().split())
dicts = defaultdict(int)
for i in range(1, N+1):
    name = input().rstrip()
    dicts[name] = str(i)
    dicts[str(i)] = name

for _ in range(M):
    print(dicts[input().rstrip()])