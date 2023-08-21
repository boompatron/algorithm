parent = [[(_, __) for _ in range(51)] for __ in range(51)]
menu = [['EMPTY' for _ in range(51)] for __ in range(51)]
answer = []


def get_parent(x, y):
    x, y = int(x), int(y)
    if parent[y][x] != (x, y):
        parent[y][x] = get_parent(parent[y][x][0], parent[y][x][1])
    return parent[y][x]


def union_parent(x1, y1, x2, y2):  # 그냥 앞의 좌표로 뒤의 좌표를 합침
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    x1, y1 = get_parent(x1, y1)
    x2, y2 = get_parent(x2, y2)
    parent[y2][x2] = parent[y1][x1]


def update_coord(x, y, val):
    # 루트 좌표를 가져온 다음에
    x, y = get_parent(x, y)
    # 루트 좌표에 해당하는 값을 업데이트 시킴
    menu[y][x] = val


def update_val(v1, v2):
    # 그냥 무식하게 돌리면서 확인하기!
    for i in range(51):
        for j in range(51):
            tx, ty = get_parent(j, i)
            if menu[ty][tx] == v1:
                menu[ty][tx] = v2


def merge(x1, y1, x2, y2):
    x1, y1 = get_parent(x1, y1)
    x2, y2 = get_parent(x2, y2)
    # 두 셀은 이제 같은 값을 가지고 있음
    # 두 셀 모두 값을 가지고 있는 경우 r1, c1의 값으로 병합됨
    # 루트 좌표를 갱신

    if menu[y1][x1] != 'EMPTY':
        union_parent(x1, y1, x2, y2)
        for i in range(1, 51):
            for j in range(51):
                if get_parent(j, i) == (x2, y2):
                    parent[i][j] = (x1, y1)
    else:
        union_parent(x2, y2, x1, y1)
        for i in range(1, 51):
            for j in range(51):
                if get_parent(j, i) == (x1, y1):
                    parent[i][j] = (x2, y2)


def unmerge(x, y):
    # 우선 값을 해제 하기 위해서 루트 좌표 값을 가져옴
    rx, ry = get_parent(x, y)
    value = menu[ry][rx]

    # 집합을 해체함
    # 만약 해당 집합에 값이 있다면 명령어 뒤에 나오는 좌표가 값을 가져감
    # 나머지 셀들은 프로그램 초기 상태로 돌아감

    merge_list = []

    for i in range(1, 51):
        for j in range(1, 51):
            tx, ty = get_parent(j, i)
            if (tx, ty) == (rx, ry):
                # 그룹에 속하는 좌표는 원래대로 돌려놓기
                parent[i][j] = (j, i)
                menu[i][j] = 'EMPTY'
                merge_list.append((j, i))
    # r, c 가 그룹의 값을 가지고 감
    menu[int(y)][int(x)] = value


def add_to_ans(x, y):   # 루트 좌표 값을 가지고 감
    rx, ry = get_parent(x, y)
    answer.append(menu[ry][rx])


def solution(commands):

    for command in commands:
        c = command.split(' ')
        if c[0] == 'UPDATE':   # 갱신
            if len(c) == 4:  # 좌표에 값 넣기
                update_coord(c[1], c[2], c[3])
            else:  # V1 의 모든 셀을 V2 로 값을 변경한다
                update_val(c[1], c[2])
        elif c[0] == 'MERGE':  # 병합
            merge(c[1], c[2], c[3], c[4])
        elif c[0] == 'UNMERGE':  # 병합 해제
            unmerge(c[1], c[2])
        else:  # 출력
            add_to_ans(c[1], c[2])
    return answer
