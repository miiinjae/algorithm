import sys

num = sys.stdin.readline()

a, b = num.split()
list = []
for i in range(int(a), int(b)+1):
    list.append(i)

for j in range(len(list)):
    num = list[j]
    if num == 1:
        continue
    for k in range(2, int(num**0.5)+1):
        if num%k == 0:
            break
    else:
        print(num)


