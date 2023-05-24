import sys

N = int(input())
meeting = []
answer = 0

for _ in range(N):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    meeting.append((start, end))
meeting.sort(key=lambda x: x[0])
meeting.sort(key=lambda x: x[1])

endTime = 0
for start, end in meeting:
    if endTime <= start:
        endTime = end
        answer += 1

print(answer)