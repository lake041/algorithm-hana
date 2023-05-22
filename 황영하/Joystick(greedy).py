spel = ' '.join("QWERTYUIOPASDFGHJKLZXCVBNM").split()
spel.sort()

def solution(name):
    res = 0
    btn = [0] * (len(name)) # 누르는 횟수
    for i in range(len(name)):
        s = spel.index(name[i])
        if s > 13: s = 26 - s
        btn[i] = s
        res += s
    move = 10e9
    for i in range(len(btn)):
        next = i + 1  # 다음 노드
        while next < len(btn) and btn[next] == 0:  # A의 연속되는 개수 체크
            next += 1
        move = min(move, i * 2 + (len(btn) - next), (len(btn) - next) * 2 + i)  # 기존, 앞 -> 뒤, 뒤 -> 앞
    return move + res