from collections import deque
from itertools import *

# INPUT 받아오기
N, M = map(int, input().split())
houses = deque([])
chickens = deque([])
answer = 0

for y in range(N):
    inp = input().split()
    for x in range(N):
        if inp[x] == '1':
            houses.append((x, y))
        if inp[x] == '2':
            chickens.append((x, y))

# 모든 집에서, 모든 치킨집까지의 거리 미리 계산하기
distances = deque([])
for house in houses:
    distance = [] #한 집에서 모든 치킨집까지의 거리 각각 계산
    for chicken in chickens:
        distance.append(abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
    distances.append(distance)

# M과 chickens의 개수가 같으면, min값 다 더하기
if M == len(chickens):
    answer = 0
    for dist in distances:
        answer += min(dist)
# M이 chickens의 개수보다 작으면, 경우의 수의 min 값 다 구해서 제일 작은 값 구하기
else:
    answer = 1000000
    li = [i for i in range(len(chickens))] #combination을 구하기 위한 리스트
    combination = list(combinations(li, M))
    for com in combination:
        house_to_chicken = [N*2 for _ in range(len(houses))]
        for h in range(len(houses)):
            for i in com:
                house_to_chicken[h] = min(house_to_chicken[h], distances[h][i])
        answer = min(answer, sum(house_to_chicken))

print(answer)