# import sys
#
# input = sys.stdin.readline()
# num = int(input)
# point = []
#
# for i in range(num):
#     point.append(int(input))
#
# if num == 1:
#     print(point[0])
# else:
#     sum = [0] * (num+1)
#     sum[1] = point[1]
#     sum[2] = point[1] + point[2]
#
#     for i in range(3, num+1):
#         sum[i] = max(sum[i-3]+point[i-1]+point[i], sum[i-2]+point[i])
#
#     print(sum[num])

n = int(input())
point = []

for i in range(n):
    point.append(int(input()))

if input == 1:
    print(point[0])
else:
    s = [0] * 300
    s[1] = point[1]
    s[2] = point[1] + point[2]

    for i in range(3, n):
        s[i] = max(s[i-3]+point[i-1]+point[i], s[i-2]+point[i])

    print(s[n+1])
##########################################################################
# n=int(input())
# stairs=[0]*300
# for i in range(n):
#   stairs[i]=int(input())
#
# d=[0]*300
# d[0]=stairs[0]
# d[1]=stairs[0]+stairs[1]
# d[2]=max(stairs[2]+stairs[0], stairs[2]+stairs[1])
# for i in range(3,n):
#   d[i]=max(stairs[i]+d[i-2], stairs[i]+stairs[i-1]+d[i-3])
#
# print(d[n-1])