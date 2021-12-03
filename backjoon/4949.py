# sum = 0
while 1:
    a = input()
    stack = []

    if a == ".":
        break

    for k in a:
        if k == "(" or k == "[":
            stack.append(k)
        elif k == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(')')
                break
        elif k == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(']')
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")


# for k in a:
#     if k == "(" or "[":
#         sum += 1
#     elif sum == 0:
#         print("NO")
#         break
#     elif k == '.':
#         break
#     else:
#         sum -= 1
#
# if sum == 0:
#     print("YES")
# elif sum > 0:
#     print("NO")
