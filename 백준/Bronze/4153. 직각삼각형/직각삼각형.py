while True:
    a, b, c = map(int, input().split())
    if a == 0 or b == 0 or c == 0:
        break
    max_num = 0
    el_num = [0, 0]
    if a > b and a > c:
        max_num = a
        el_num[0] = b; el_num[1] = c
    elif b > a and b > c:
        max_num = b
        el_num[0] = a; el_num[1] = c
    else:
        max_num = c
        el_num[0] = a; el_num[1] = b
    if max_num ** 2 == el_num[0] ** 2 + el_num[1] ** 2:
        print("right")
    else:
        print("wrong")
