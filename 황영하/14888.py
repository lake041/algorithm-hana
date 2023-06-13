import sys


def bt(s):
    # print(s)
    if len(s) == (n-1):  # 길이 충족
        order.append(s)
        return
    for i in range(4):
        if op[operator[i]] > 0:
            op[operator[i]] -= 1
            bt(s + operator[i])
            op[operator[i]] += 1
    return


operator = ['+', '-', '*', '/']
n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))  # 숫자
tmp = list(map(int, sys.stdin.readline().split()))
op = dict()  # 연산자
for i in range(4): op[operator[i]] = tmp[i]
order = list()  # 연산순서(문자열)
bt("")
# print(order)

max_val = (-1) * (int(10e9))  # 최소값 : -10억
min_val = int(10e9)   # 최대값 : 10억(10e9)

for i in range(len(order)):
    tmp = nums[0]
    for j in range(n-1):
        if order[i][j] == "+":
            tmp += nums[j+1]
        elif order[i][j] == '-':
            tmp -= nums[j+1]
        elif order[i][j] == "*":
            tmp *= nums[j+1]
        elif order[i][j] == "/":
            tmp /= nums[j+1]
            tmp = int(tmp)
    max_val = max(max_val, tmp)
    min_val = min(min_val, tmp)

print(max_val)
print(min_val)