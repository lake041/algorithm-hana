import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
graph = list()
house = list()  # 집의 좌표
chicken = list()  # 치킨집 좌표

for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append([i, j])
        elif graph[i][j] == 2:
            chicken.append([i, j])

res = int(1e9)  # 도시의 치킨거리
for pick in combinations(chicken, m):  # 모든 치킨집 중에서 m개 뽑은 케이스
    temp = 0
    for h in house:
        d = 10000  # 하나의 가구의 치킨거리
        for p in pick:
            d = min(d, abs(h[0]-p[0]) + abs(h[1]-p[1]))
        temp += d
    res = min(res, temp)
print(res)