import sys

T = int(sys.stdin.readline())
one = [0] * 41
zero = [0] * 41
one[0] = 0
one[1] = 1

zero[0] = 1
zero[1] = 0

for i in range(T):
    num = int(sys.stdin.readline().strip())

    if num <= 1:
        print(zero[num], one[num])
    elif num > 1:
        for i in range(2, num + 1):
            zero[i] = zero[i - 1] + zero[i - 2]
            one[i] = one[i - 1] + one[i - 2]
        print(zero[num], one[num])
