from collections import deque

def D(n):
    return (n * 2) % 10000

def S(n):
    return n - 1 if n > 0 else 9999

def L(n):
    return (n % 1000) * 10 + n // 1000
    # return int(str(n)[1:]+str(n)[0])

def R(n):
    return (n % 10) * 1000 + n // 10
    # return int(str(n)[-1]+str(n)[0:-1])

def BFS(start, target, visited):
    q = deque([(start, '')])
    visited[start] = True
    while q:
        c, cmds = q.popleft()
        if c == target:
            return cmds
        else:
            adjs = [(D(c), 'D'), (S(c), 'S'), (L(c), 'L'), (R(c), 'R')]
            for adj, cmd in adjs:
                if not visited[adj]:
                    visited[adj] = True
                    q.append((adj, cmds + cmd))

N = int(input())
for _ in range(N):
    A, B = map(int, input().split());
    visited = [False for _ in range(10000)]
    print(BFS(A, B, visited))
