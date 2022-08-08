import sys


def solution():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    josephus, pos, ans = [_ for _ in range(1, n + 1)], k - 1, []
    for i in range(n):
        ans.append(josephus[pos % n])
        josephus = josephus[:pos] + josephus[pos + 1:]
        if not josephus:
            break
        pos += k - 1
        pos = pos % len(josephus)
    print('<' + ', '.join(map(str, ans)) + '>')


if __name__ == "__main__":
    solution()