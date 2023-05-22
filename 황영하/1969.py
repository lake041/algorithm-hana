import sys

n, m = map(int, sys.stdin.readline().split())
dna = list()
res = ""
dist = 0
for _ in range(n):
    t = sys.stdin.readline().rstrip()  # dna 입력
    dna.append(t)

for i in range(m):
    check = dict()
    for s in dna:
        if s[i] not in check:
            check[s[i]] = 0
        check[s[i]] += 1
    v = max(check.values())  # 각 인덱스의 가장 많이 나온 숫자 확보
    t = list(check.keys())
    t.sort()
    for j in t:
        if check[j] == v:
            res += j  # dna 생성
            break
dist = 0
# 체크
for i in dna:
    check = -1
    temp = 0
    for j in range(m):
        if i[j] != res[j]:  # 서로 문자가 다른 경우
            dist += 1  # 추가

print(res)
print(dist)