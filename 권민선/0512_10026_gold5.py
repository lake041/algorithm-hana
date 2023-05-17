import sys
from collections import deque

def BFS(graph, start, visited):
    q = deque([start])
    cx = start[0]
    cy = start[1]
    visited[cx][cy] = True
    target = graph[cx][cy]
    while q:
        tx, ty = q.popleft()
        adjs =[]
        for i in range(4):
            nx = tx+dx[i]
            ny = ty+dy[i]
            if nx < N and ny < N and nx >= 0 and ny >= 0:
                adjs.append((tx+dx[i], ty+dy[i]))
        for x, y in adjs:
            if not visited[x][y] and target == graph[x][y]:
                q.append((x, y))
                visited[x][y] = True

def BFS_FOR_RG(graph, start, visited):
    q = deque([start])
    cx = start[0]
    cy = start[1]
    visited[cx][cy] = True
    target = graph[cx][cy]
    while q:
        tx, ty = q.popleft()
        adjs =[]
        for i in range(4):
            nx = tx+dx[i]
            ny = ty+dy[i]
            if nx < N and ny < N and nx >= 0 and ny >= 0:
                adjs.append((tx+dx[i], ty+dy[i]))
        for x, y in adjs:
            if not visited[x][y]:
                if target == graph[x][y]or (target in ["R", "G"] and graph[x][y] in ["R", "G"]):
                    q.append((x, y))
                    visited[x][y] = True


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
graph = []
for i in range(N):
    graph.append(list(sys.stdin.readline().rstrip()))

visited = [[False for _ in range(N)] for _ in range(N)]
visited2 = [[False for _ in range(N)] for _ in range(N)]
ans = 0
ans2 = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            ans += 1
            BFS(graph, (i, j), visited)

for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            ans2 += 1
            BFS_FOR_RG(graph, (i, j), visited2)

print(ans, ans2)