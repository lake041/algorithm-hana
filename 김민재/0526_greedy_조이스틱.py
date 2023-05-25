# 조이스틱
# https://school.programmers.co.kr/learn/courses/30/lessons/42860
# 구글링으로 멋있는 풀이를 찾았지만 그건 도저히 이해가 안 감
# 이 풀이는 통과되는 게 도저히 이해가 안 감

from itertools import permutations


def solution(name):
    answer = 0
    for char in name:
        x = abs(ord(char)-ord('A'))
        y = abs(ord(char)-ord('Z')-1)
        answer += min(x, y)

    cnt = 25555
    destinations = [i for i in range(1, len(name)) if name[i] != 'A']
    for route in permutations(destinations):
        now = 0
        temp = 0
        for next in route:
            distance = min(abs(now-next), len(name)-abs(now-next))
            temp += distance
            now = next
        cnt = min(cnt, temp)
    answer += cnt

    return answer


# 그때 그때 최단거리에 위차한 인덱스로 움직이는 풀이 (오답)
'''
def solution(name):
    answer = 0
    for char in name:
        x = abs(ord(char)-ord('A'))
        y = abs(ord(char)-ord('Z')-1)
        answer += min(x, y)

    list_name = list(name)
    end = ['A' for _ in range(len(list_name))]
    i = 0
    list_name[0] = 'A'
    while True:
        if list_name == end:
            break
        temp = [255 for _ in range(len(list_name))]
        for j, char in enumerate(list_name):
            if char == 'A':
                continue
            temp[j] = min(abs(i-j), len(list_name)-abs(i-j))
        i = temp.index(min(temp))
        list_name[i] = 'A'
        answer += min(temp)

    return print(answer)
'''
