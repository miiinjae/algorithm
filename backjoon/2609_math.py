import sys

c, d = sys.stdin.readline().split()

a = int(c)
b = int(d)

r = 1

while r != 0:
    if b == 0:
        break
    elif a > b:
        r = a%b
        a, b = b, r
        cm = a
    elif a < b:
        a, b = b, a
    elif a%b == 0:
        cm = b
        r = 0

print(cm)
print((int(c)*int(d))//cm)


