import sys
# https://m.blog.naver.com/ndb796/221282210534 안경잡이 개발자 세그먼트 트리

n, m, k = map(int, sys.stdin.readline().rstrip().split())
tree = [0 for _ in range((n + 1) * 4)]
g = [int(sys.stdin.readline().rstrip()) for _ in range(n)]


# start, end : 시작, 끝 인덱스
def init_tree(start: int, end: int, node: int):
    if start == end:
        tree[node] = g[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init_tree(start, mid, node * 2) + init_tree(mid + 1, end, node * 2 + 1)
    return tree[node]


# start: 시작 인덱스, end : 끝 인덱스
# left, right: 구간 합을 구하고자 하는 범위
def prefix_sum(start: int, end: int, node: int, left: int, right: int):
    #  범위 밖인 경우
    if left > end or right < start:
        return 0

    # 범위 안에 있는 경우
    if left <= start and end <= right:
        return tree[node]

    # 그것도 아니라면 두 부분으로 나누어서 합을 구하자
    mid = (start + end) // 2
    return prefix_sum(start, mid, node * 2, left, right) + prefix_sum(mid + 1, end, node * 2 + 1, left, right)


# start: 시작 인덱스, end : 끝 인덱스
# index: 구간 합을 수정하고자 하는 노드
# diff: 수정할 값
def update_tree(start: int, end: int, node: int, index: int, diff: int):
    #  범위 밖인 경우
    if index > end or index < start:
        return

    # 범위 안에 있으면 내려가면서 다른 원소도 갱신
    tree[node] += diff

    if start == end:
        return

    mid = (start + end) // 2
    update_tree(start, mid, node * 2, index, diff)
    update_tree(mid + 1, end, node * 2 + 1, index, diff)


init_tree(0, n - 1, 1)
for i in range(m + k):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 2:
        print(prefix_sum(0, n - 1, 1, b - 1, c - 1))
    else:
        diff = c - g[b - 1]
        g[b - 1] = c
        update_tree(0, n - 1, 1, b - 1, diff)
