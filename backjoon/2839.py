import sys

num = int(sys.stdin.readline())
count = [0] * 5000

for i in range(3, num + 1):
    count[i] = count[i - 1] + 1
    if i % 3 == 0:
        count[i] = min(count[i], count[i // 3] + 1)
    if i % 5 == 0:
        count[i] = min(count[i], count[i // 5] + 1)
    if i % 3 != 0 and i % 5 != 0:
        count[i] = 10000

if count[num] < 10000:
    print(count[num])
else:
    print(-1)

# 어디서 막혔는지
# 이렇게 접근한 이유
# 간략한 코드 설명