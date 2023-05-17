"""
1. heap 한개로 하다 실패
2. min, max힙 구현했지만 deleted = []를 썼다가 런타임오류
3. 결국 visited로 구현
"""
import heapq

T = int(input())

for _ in range(T):
    K = int(input())
    min_h = []
    max_h = []
    visited = [False] * K
    for i in range(K):
        cmd, n = input().split()
        n = int(n)
        if cmd == "I":
            heapq.heappush(min_h, (n, i))
            heapq.heappush(max_h, (-n, i))
            visited[i] = True
        else:
            if n == -1:
                while min_h and not visited[min_h[0][1]]: heapq.heappop(min_h)
                if min_h:
                    visited[min_h[0][1]] = False
                    heapq.heappop(min_h)
            else:
                while max_h and not visited[max_h[0][1]]: heapq.heappop(max_h)
                if max_h:
                    visited[max_h[0][1]] = False
                    heapq.heappop(max_h)


    while min_h and not visited[min_h[0][1]]: heapq.heappop(min_h)
    while max_h and not visited[max_h[0][1]]: heapq.heappop(max_h)

    if min_h and max_h:
        print(-max_h[0][0], min_h[0][0])
    else:
        print("EMPTY")