N = int(input())
arr = list(map(int, input().split()))
target = -1

# 오름차순 되어있지 않은 target의 index를 찾는다.
for i in range(N - 1, 0, -1):
    if arr[i - 1] > arr[i]:
        target = i - 1
        break

# 오름차순으로 되어 있으면
if target == -1:
    print(-1)
else:
    # 뒤에서 부터 target보다 작은 수를 찾고, swap
    for i in range(N - 1, 0, -1):
        if arr[i] < arr[target]:
            arr[i], arr[target] = arr[target], arr[i]
            break
    a = arr[:target + 1] + sorted(arr[target + 1:], reverse=True) #기준이된 target 이후의 수를 다시 내림차순으로 정렬
    print(*a)

# 날먹하려다가 메모리 초과
"""
from itertools import permutations

N = int(input())
input = tuple(map(int, input().split()))
list_for_permutation = [i for i in range(1, N+1)]
permutation = list(permutations(list_for_permutation, N))

if permutation[0] == input:
    print(-1)
else:
    for i in range(1, len(permutation)):
        if permutation[i] == input:
            print(' '.join(list(map(str, permutation[i-1]))))
"""