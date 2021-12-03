import sys

T = int(sys.stdin.readline())
result = T
for i in range(T):
    h, w, n = map(int, (sys.stdin.readline().split()))

    if n % h == 0:
        floor = h * 100
        room = n // h
    else:
        floor = (n % h) * 100
        room = (n // h) + 1

    print(floor + room)


