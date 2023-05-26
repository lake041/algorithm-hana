# Contact
# https://www.acmicpc.net/problem/1013
# greedy
# re 안 쓰고 어거지로 풀다가 포기함
# 정규표현식 어느 정도까지 공부해야할지 모르겠음

import re
from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    string = input().rstrip()
    regex = re.compile('(100+1+|01)+')
    checked = regex.fullmatch(string)
    if checked:
        print('YES')
    else:
        print('NO')

'''
from sys import stdin
input = stdin.readline

def first(string, isEnd):
    # 100001111001
    if len(string) >= 1 and string[0] != '1': return False
    if len(string) >= 2 and string[1] != '0': return False
    if len(string) >= 3 and string[2] != '0': return False
    if len(string) >= 4 and string[-1] == '1': return 'Yes'
    return False if isEnd else 'Hold'

def second(string, isEnd):
    if len(string) == 1 and string == '1': return False
    if len(string) == 2 and string == '01': return 'Yes'
    if len(string) >= 3: return False
    return False if isEnd else 'Hold'

T = int(input())
for _ in range(T):
    case = input().rstrip()
    isTrue = True
    temp = ''
    if case == '10':
        print('YES')
        continue
    for i in range(len(case)):
        if i == len(case)-1:
            isEnd = True
        else:
            isEnd = False

        temp += case[i]
        if second(temp, isEnd)=='Yes':
            temp = ''
        elif first(temp, isEnd)=='Yes':
            # 10011001001
            if isEnd == True:
                temp = ''
            # 3. 1001 0 1
            # 4. 1001 0 0
            elif case[i+1] == '0':
                temp = ''
            # 1. 1001 1 1 1
            # 1. 1001 1 1 0
            # 2. 1001 1 0 0
            # 2. 1001 1 0 1
            elif i+2<len(case) and case[i+2] == '0':
                temp = '1'
            else:
                temp = ''
        elif first(temp, isEnd)=='Hold' or second(temp, isEnd)=='Hold':
            pass
        else:
            isTrue = False
            break

    if isTrue:
        print('YES')
    else:
        print('NO')
'''

'''
(100+1+ | 01)+

"100"000"11"111 또는 "01" 
'''
