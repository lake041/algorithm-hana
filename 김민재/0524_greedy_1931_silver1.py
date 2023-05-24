# 회의실 배정
# https://www.acmicpc.net/problem/1931
# greedy
# 끝나는 시간 -> 시작 시간 순으로 정렬

from sys import stdin
input = stdin.readline

N = int(input())
arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append([start, end])
arr.sort(key = lambda x : (x[1], x[0]))

ans = 0
now = 0
for conference in arr:
    start, end = conference
    if now <= start:
        ans += 1
        now = end
print(ans)