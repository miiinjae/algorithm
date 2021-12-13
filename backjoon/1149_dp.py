import sys

T = int(sys.stdin.readline())
house = []

for i in range(T):
    house.append(list(map(int, input().strip().split())))

for i in range(1, T):
    house[i][0] += min(house[i - 1][1], house[i - 1][2])
    house[i][1] += min(house[i - 1][0], house[i - 1][2])
    house[i][2] += min(house[i - 1][0], house[i - 1][1])

print(min(house[T - 1]))
