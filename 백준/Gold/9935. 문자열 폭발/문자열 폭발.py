import sys


def solution():
    l1 = sys.stdin.readline().rstrip()
    l2 = sys.stdin.readline().rstrip()
    stack = []
    for l in l1:
        stack.append(l)
        if l == l2[-1] and ''.join(stack[-len(l2):]) == l2:
            for i in range(len(l2)):
                stack.pop()
    print(''.join(stack) if stack else 'FRULA')


if __name__ == "__main__":
    solution()
