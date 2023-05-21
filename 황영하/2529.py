import sys

def check(s, idx):  # 숫자, 체크할 인덱스
    # print(s)
    if idx == k:
        global max_val
        global min_val
        max_val = max(max_val, int(s))
        min_val = min(min_val, int(s))
    else:
        for i in range(10):
            if str(i) in s:  # 이미 숫자가 있는 경우
                continue # 패스
            else:
                if comp[idx] == '>' and int(s[-1]) > i:
                    check(s + str(i), idx+1)
                elif comp[idx] == '<' and int(s[-1]) < i:
                    check(s + str(i), idx+1)
    return


max_val = 0
min_val = 10e9

k = int(sys.stdin.readline())
comp = ' '.join(sys.stdin.readline().rstrip()).split()  # 부등호

for i in range(10):
    check(str(i), 0)
print(str(max_val))
print(str(min_val).zfill(k+1))
