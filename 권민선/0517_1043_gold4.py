from collections import deque

N, M = map(int, input().split())
dirty = list(map(int, input().split()))
parties = []

for _ in range(M):
    parties.append(set(list(map(int, input().split()))[1:]))

if dirty[0] == 0:
    print(M)

else:
    dirty = set(dirty[1:])

    for _ in range(M):
        for party in parties:
            if party & dirty:
                dirty = dirty.union(party)

    answer = 0
    for party in parties:
        if party & dirty:
            continue
        else:
            answer+=1
    print(answer)