import sys
from collections import deque
opening_bracket = '('
closing_bracket = ')'
low_priority = ('+', '-')
high_priority = ('*', '/')

ans = ''
operator_stack = deque()
g = sys.stdin.readline().rstrip()
for i in g:
    if i in high_priority or i in low_priority:
        if operator_stack and i in low_priority:
            while operator_stack and (operator_stack[-1] in high_priority or operator_stack[-1] in low_priority):
                ans += operator_stack.pop()
        if operator_stack and i in high_priority:
            while operator_stack and operator_stack[-1] in high_priority:
                ans += operator_stack.pop()
        operator_stack.append(i)
    elif i == opening_bracket:
        operator_stack.append(i)
    elif i == closing_bracket:
        while operator_stack[-1] != opening_bracket:
            ans += operator_stack.pop()
        operator_stack.pop()
    else:
        ans += i
while operator_stack:
    top = operator_stack.pop()
    if top != opening_bracket and top != closing_bracket:
        ans += top
print(ans)
