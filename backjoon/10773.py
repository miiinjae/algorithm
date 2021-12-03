import sys
T = int(sys.stdin.readline())
stack = []
sum = 0

for i in range(T):
    a = sys.stdin.readline().split()
    if a[0] != '0':
        stack.append(a[0])
    else:
        stack.pop()

for k in range(len(stack)):
    sum += int(stack.pop())
print(sum)