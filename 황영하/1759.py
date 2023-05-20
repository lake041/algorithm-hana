import sys

def dfs(s, idx):
    if len(s) == L:  # 암호문 가능한 경우
        cnt = 0  # 모음의 개수
        for i in s:
            if i in gat: cnt += 1
        if cnt > 0 and (L-cnt) > 1:
            print(s)
    for i in range(idx, C):
        dfs(s + a[i], i+1)
    return


L, C = map(int, sys.stdin.readline().split())  # 암호문 길이, 알파벳 개수
a = ' '.join(sys.stdin.readline().rstrip()).split()
gat = dict()
a.sort()
for i in a:
    if i in ['a', 'i', 'e', 'o', 'u']:  # 모음 체크
        gat[i] = 1

for i in range(C-L+1):
    dfs(a[i], i+1)
