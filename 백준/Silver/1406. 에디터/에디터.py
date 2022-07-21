import sys


def solution():
    s1, s2 = list(sys.stdin.readline().rstrip()), []
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        inst = sys.stdin.readline().rstrip()
        if inst[0] == 'P':
            s1.append(inst[2:])
        elif inst[0] == 'B' and s1:
            s1.pop()
        elif inst[0] == 'L' and s1:
            s2.append(s1.pop())
        elif inst[0] == 'D' and s2:
            s1.append(s2.pop())
    print(''.join(s1) + ''.join(reversed(s2)))


if __name__ == "__main__":
    solution()
