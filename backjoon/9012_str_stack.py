import sys

T = int(sys.stdin.readline())

# for i in range(T):
#     a = sys.stdin.readline().strip()
#     stack = []
#     for k in a:
#         if k == "(":
#             stack.append(k)
#         elif k == ")":
#             if stack:
#                stack.pop()
#             else:
#                 stack.append(")")
#                 break
#     if len(stack) == 0:
#         print("YES")
#     else:
#         print("NO")

# for i in range(T):
#     a = list(sys.stdin.readline().strip())
#     sum = 0
#
#     for k in a:
#         if k == "(":
#             sum += 1
#         elif k == ")":
#             # if sum == 0:
#             #     print("NO")
#             #     break
#             sum -= 1
#         if sum < 0:
#             print("NO")
#             break
#
#     if sum == 0:
#         print("YES")
#     elif sum > 0:
#         print("NO")

# for i in range(T):
#     a = list(sys.stdin.readline().strip())
#     sum = 0
#
#     for k in a:
#         if k == "(":
#             sum += 1
#         elif sum == 0:
#             print("NO")
#             break
#         else:
#             sum -= 1
#
#     if sum == 0:
#         print("YES")
#     elif sum > 0:
#         print("NO")