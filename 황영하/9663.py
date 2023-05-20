import sys

def check(x): # 퀸과 만나는지 체크
    for i in range(x):
        if (col[x] == col[i]) or (abs(col[i] - col[x]) == (x - i)): # 각각 같은 행, 대각선 체크
            return False
    return True # 만나지 않을 때 True 리턴

def dfs(d):
    global cnt
    if d == n: # 전부 다 채웠으면
        cnt += 1 # 개수 증가
        # print(col) #디버그
        return
    for i in range(n):
        col[d] = i
        if check(d): # 해당 자리의 적절 여부 체크
            dfs(d+1) # True라면 다음 자리 체크

n = int(sys.stdin.readline())
cnt = 0
col = [0] * n
dfs(0)
print(cnt)

# 참조 : https://zidarn87.tistory.com/339