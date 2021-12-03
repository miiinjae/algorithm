import sys

num = sys.stdin.readline()

a, b = num.split()
a = int(a)
b = int(b)
result = 1
result2 = 1
result3 = 1
for i in range(1, a + 1, 1):
    result *= i

for i in range(1, (a - b) + 1, 1):
    result2 *= i

for i in range(1, b + 1, 1):
    result3 *= i

print(result//(result3*result2))
