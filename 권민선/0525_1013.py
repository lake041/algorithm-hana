# 문자열 매칭 문제는 문자열 매칭을 쓰자...
import sys
import re

N = int(input())
results = []

for _ in range(N):
    input = sys.stdin.readline().rstrip()
    regex = re.compile('(100+1+|01)+')
    answer = regex.fullmatch(input)
    print("YES" if answer else "NO")

"""import sys
from collections import deque

N = int(input())
for _ in range(N):
    q = deque(list(sys.stdin.readline().rstrip()))
    answer = True

    while q and answer:
        if len(q) == 1:
            answer = False
        else:
            nxt = q.popleft()+q.popleft()
            if nxt == "01":
                continue
            elif nxt == "10":
                if len(q) < 2: #10 뒤에 0과 1이 최소 한번씩은 나와야 하기 때문에 q가 0, 1이면 False
                    answer = False
                    break
                nnxt = q.popleft()
                if nnxt != "0": #10뒤에 바로 0이 아니면 False
                    answer = False
                    break
                while nnxt == "0" and q: #q가 비었거나, nnxt가 0이 아니면(1이면) STOP
                    nnxt = q.popleft()
                if nnxt == "0" and not q: #nnxt가 1이 아니거나, q가 비었으면 False
                    answer = False
                    break
                while nnxt == "1" and q:
                    nnxt = q.popleft()
                if q: #q가 빈게 아니라면, 마지막에 pop한 숫자를 다시 넣어주기
                    q.appendleft(nnxt)
            else:
                answer = False

    print("YES" if answer else "NO")"""