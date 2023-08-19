min_cnt = 0x3f3f3f3f
num_int = 0
btn_set = {i for i in range(0, 10)}


def find(num):
    global min_cnt, num_int, btn_set

    for btn in btn_set:
        tmp_num = num + str(btn)
        min_cnt = min(min_cnt, abs(num_int - int(tmp_num)) + len(tmp_num))

        if len(tmp_num) < 6:
            find(tmp_num)


def main():
    global min_cnt, num_int, btn_set

    num_int = int(input())
    n = int(input())

    min_cnt = min(min_cnt, abs(100 - num_int))
    btn_set -= set(map(int, input().split(' '))) if n else set()

    find('') if n < 10 else ''
    print(min_cnt)


main()