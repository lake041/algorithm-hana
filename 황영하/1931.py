import sys

n = int(sys.stdin.readline())
lec = list()
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    lec.append([start, end])
lec.sort()
lec.sort(key = lambda x : x[1])  # 가장 빨리 끝나는 강의 중 가장 이른 강의
e = 0  # 종료시간
res = 0

for i in range(len(lec)):
    if lec[i][0] >= e:  # 시작 가능
        res += 1
        e = lec[i][1]
print(res)