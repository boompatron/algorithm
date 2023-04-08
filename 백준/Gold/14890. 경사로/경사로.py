import sys


def solution():
    n, l = map(int, sys.stdin.readline().rstrip().split())
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    tmp = list(map(list, zip(*g)))

    def check(array: list):
        length = 1
        last_change = 1
        if array[0] == array[1]:
            last_change = 0
        elif array[0] > array[1]:
            last_change = -1
        for i in range(1, n):
            if array[i - 1] == array[i]:
                length += 1
            elif array[i - 1] < array[i]: # 경사가 높아지는 경우
                if last_change == 1 and length < l or last_change == -1 and length < 2 * l or last_change == 0 and length < l:
                    return False
                if abs(array[i - 1] - array[i]) > 1:
                    return False
                last_change = 1
                length = 1
            else: # 경사가 낮아지는 경우
                if abs(array[i - 1] - array[i]) > 1:
                    return False
                if i == 1:
                    continue
                if last_change == -1 and length < l:
                    return False
                length = 1
                last_change = -1
        if length < l and last_change == -1:
            return False
        return True

    cnt = 0
    for i in range(n):
        cnt += int(check(g[i])) + int(check(tmp[i]))
    print(cnt)


if __name__ == '__main__':
    solution()
