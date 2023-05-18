#1. 1번 노드에서 제일 거리가 긴 노드 X를 찾고
#2. X에서 제일 거리가 먼 노드를 찾는다. <-- !important
from collections import defaultdict


def dfs(visited, start, dist):
    visited[start] = dist
    for adj, cost in tree[start]:
        if not visited[adj]:
            dfs(visited, adj, dist+cost)


V = int(input())
tree = defaultdict(list)

for _ in range(V):
    ins = list(map(int, input().split()))
    for i in range(1, len(ins) - 1, 2):
        tree[ins[0]].append((ins[i], ins[i+1]))

v = [0 for _ in range(V+1)]
dfs(v, 1, 1)
idx = v.index(max(v)) #제일 먼 노드 찾기

v = [0 for _ in range(V+1)]
dfs(v, idx, 1) #다시 DFS

print(max(v)-1)