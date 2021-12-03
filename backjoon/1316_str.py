# import sys
#
# T = int(sys.stdin.readline())
# result = T
# for i in range(T):
#     word = sys.stdin.readline().strip()
#     for idx in range(len(word)-1):
#         if word[idx] == word[idx+1]:
#             pass
#         elif word[idx] in word[idx+1:]:
#             result -= 1
#             break
#
# print(result)

import sys

T = int(sys.stdin.readline())
result = T
for i in range(T):
    word = sys.stdin.readline().strip()
    for idx in range(len(word)-1):
        if word[idx] != word[idx+1]:
            if word[idx] in word[idx+2:]:
                result -= 1
                break

print(result)