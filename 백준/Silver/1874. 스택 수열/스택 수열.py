import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    stack, ans, cur = [], [], 1
    flag = True
    for i in range(n):
        a = int(sys.stdin.readline().rstrip())
        while a >= cur:
            stack.append(cur)
            cur += 1
            ans.append('+')
        while stack and stack[-1] != a:
            stack.pop()
        if stack and stack[-1] == a:
            stack.pop()
            ans.append('-')
        else:
            flag = False
    print('\n'.join(ans) if flag else 'NO')


if __name__ == "__main__":
    solution()
