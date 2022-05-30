import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = list(map(int, sys.stdin.readline().rstrip().split()))
    left, right, diff = 0, n - 1, sys.maxsize
    ans = [0, 0]
    while left != right:
        cur_diff = g[left] + g[right]
        if abs(cur_diff) < diff:
            diff = abs(cur_diff)
            ans = [g[left], g[right]]
        if cur_diff > 0:
            right -= 1
        elif cur_diff < 0:
            left += 1
        else:
            break
    for a in ans:
        print(a, end=" ")


if __name__ == "__main__":
    solution()
