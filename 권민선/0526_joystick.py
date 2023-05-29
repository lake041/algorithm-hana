import re

def getIdxMaxA(name):
    findAll = re.findall("A+", name)
    if not findAll:
        return len(name) - 1
    regex = re.compile(max(findAll))
    idx = regex.search(name).span()
    return idx

def right_straight(arr): #오른쪽에서 A가 아닌 문자가 시작하는 위치 찾기
    ans = 0
    for ar in arr[::-1]:
        if ar == 0:
            ans += 1
        else:
            break
    return len(arr) - ans

def left_straight(arr): # 왼쪽에서 A가 아닌 문자가 시작하는 위치 찾기
    ans = 0
    for ar in arr:
        if ar == 0:
            ans += 1
        else:
            break
    return len(arr) - ans

def solution(name):
    answer = 0
    for i in range(len(name)):
        temp = ord(name[i]) - 65
        answer += min(temp, 26-temp)

    if answer == 0: # ALL chars is "A"
        return answer

    max_a = getIdxMaxA(name) #제일 긴 A의 (시작 인덱스, 끝 인덱스)를 re를 사용해서 받아오기
    
    if max_a == len(name) - 1:
        return answer + len(name) - 1
    else:
        right_to_left = ((max_a[0] - 1) * 2) + (len(name) - max_a[1])
        left_to_right = ((len(name) - max_a[1] + 1) * 2) + (max_a[0] - 3)
        right = right_straight(name)
        left = left_straight(name)

        return answer + min(right_to_left, left_to_right, right, left)

# print(solution("JEROEN")) #56
# print(solution("JAZ")) #11
# print(solution("AAAA")) #0
# print(solution("JAN")) #23
# print(solution("BAABAAB")) # 7
# print(solution("CAAAAAC")) # 5
#
# print(solution("ABABAAAAABA")) # 10
# print(solution("ABAAAAABABA")) # 9
# print(solution("AAAAABBAAAAAAABAAA")) # 13 + 3 ->  92.6점일때 통과 못한 테스트 케이스 (왼쪽 쭉이 이득인 케이스)