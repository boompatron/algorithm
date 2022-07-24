import sys
n = int(input())
stack = []
while n:
    instruction = str(sys.stdin.readline())
    if instruction[:3] == 'pus':        #push
        num = 0
        num = int(instruction[5:-1])
        stack.append(num)
    elif instruction[:3] == 'pop':
        if len(stack):
            print(stack.pop(len(stack) - 1))
        else:
            print(-1)
    elif instruction[:3] == 'siz':
        print(len(stack))
    elif instruction[:3] == 'emp':
        if len(stack):
            print(0)
        else:
            print(1)
    elif instruction[:3] == 'top':
        if len(stack):
            print(stack[len(stack) - 1])
        else:
            print(-1)
    n -= 1