import sys

N, M = map(int, sys.stdin.readline().split())
dna = []

for _ in range(N):
    dna.append(list(sys.stdin.readline().rstrip()))

answer = ''
hamming_distance = 0
for i in range(M):
    temp = [0, 0, 0, 0]
    for j in range(N):
        if dna[j][i] == 'A':
            temp[0] += 1
        elif dna[j][i] == 'C':
            temp[1] += 1
        elif dna[j][i] == 'G':
            temp[2] += 1
        else:
            temp[3] += 1
    idx = temp.index(max(temp))
    hamming_distance += (N - max(temp))
    if idx == 0:
        answer += 'A'
    elif idx == 1:
        answer += 'C'
    elif idx == 2:
        answer += 'G'
    else:
        answer += 'T'

print(answer)
print(hamming_distance)
