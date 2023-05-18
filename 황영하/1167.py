import sys

sys.setrecursionlimit(int(10e6))


def dfs(now, cost):  # 현재 노드, 1부터 현재 노드까지의 cost
    for i in graph[now]:  # now 노드와 연결된 노드, now ~ 노드까지의 거리
        node, c = i[0], i[1]
        if not visited[node]:  # 방문하지 않은 경우
            visited[node] = True  # 방문처리
            dist[node] = (cost + c)
            dfs(node, cost + c)
    return


v = int(sys.stdin.readline())  # 정점의 개수
graph = [[] for _ in range(v + 1)]
dist = [0] * (v + 1)  # 노드 1에서부터 각 노드별 거리
visited = [False] * (v + 1)  # 방문처리
for _ in range(v):
    temp = list(map(int, sys.stdin.readline().split()))
    a = temp[0]
    for i in range(1, len(temp) - 2, 2):
        b, c = temp[i], temp[i + 1]
        graph[a].append([b, c])

dfs(1, 0)
visited[1] = True
last = dist.index(max(dist))  # 지름의 끝점 -> 기준점으로
dist = [0] * (v + 1)
visited = [False] * (v + 1)
visited[last] = True  # 기준점 방문처리
dfs(last, 0)
print(max(dist))
#print(dist)