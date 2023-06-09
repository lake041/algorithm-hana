# 1. 맨 뒤가 1인가
# 2. 2로 나누어 지는가
# 3. 둘 다 안된다면 break

A, B = input().split()
answer = 1

while A!=B:
    if len(B) >= 2 and B[-1] == '1':
        B = B[:-1]
    elif int(B) % 2 == 0 and int(B) != 0:
        B = str(int(B)//2)
    else:
        answer = -1
        break
    answer += 1

print(answer)