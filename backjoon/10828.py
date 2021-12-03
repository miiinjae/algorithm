import sys

T = int(sys.stdin.readline())
stack = []
for i in range(T):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0] == 'pop':
        if stack:
            pop = stack.pop()
            print(pop)
        else:
            print('-1')
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if stack:
            print('0')
        else:
            print('1')
    elif a[0] == 'top':
        if stack:
            top = stack[-1]
            print(top)
        else:
            print(-1)
