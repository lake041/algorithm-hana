import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))  # 숫자 입력

for i in range(n-1, 0, -1):
    j = i - 1
    if a[j] > a[i]:  # 현재 수가 앞 수보다 작은 경우
        tmp = sorted(a[i:])  # 현재 수 기준으로 오름차순 정렬하는 리스트 생성
        tmp.sort(reverse=True)  # 내림차순 정렬
        # print(tmp)
        for k in range(len(tmp)):
            if a[j] > tmp[k]:  # 기준이 되는 수보다 작은 수 중에서 가장 큰 수 추출
                a[j], tmp[k] = tmp[k], a[j]  # swap
                tmp.sort(reverse=True)  # 내림차순 후 붙이기
                a[j+1:] = tmp
                print(*a)  # 출력 후 탈출(exit 없으면 TLE)
                exit()
print(-1)  # 순열 중 가장 작은 케이스(사전순으로 가장 처음에 오는 순열)