import sys
while True:
    stack = []
    isBalanced = True
    l = list(sys.stdin.readline())
    if l[0] == '.':
        break
    for i in l:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ']' or i == ')':
            if len(stack) == 0:
                isBalanced = False
            elif i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            else:
                isBalanced = False
    if len(stack) > 0:
        isBalanced = False
    if isBalanced:
        print("yes")
    else:
        print("no")
