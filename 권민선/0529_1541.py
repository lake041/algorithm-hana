from collections import deque

arr = deque(input().split("-"))
answer = 0

init = list(map(int, arr.popleft().split("+")))
for tmp in init:
    answer += tmp

for ar in arr:
    temp = list(map(int, ar.split("+")))
    for tmp in temp:
        answer -= tmp

print(answer)