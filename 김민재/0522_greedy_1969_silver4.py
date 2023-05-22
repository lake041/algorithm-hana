# DNA
# https://www.acmicpc.net/problem/1969
# greedy
# 꼼수로 점철된 풀이. 조만간 다시 풀어야겠음.

from collections import Counter
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arrs = [list(map(str, input().rstrip())) for _ in range(N)]
arrs = list(map(list, zip(*arrs[::-1])))

ans1 = ''
ans2 = 0
for arr in arrs:
    arr.sort()
    char, num = Counter(arr).most_common()[0]
    ans1 += char
    ans2 += (N-num)

print(ans1)
print(ans2)