import sys
d = {}
preorder_ans, inorder_ans, postorder_ans = '', '', ''


def preorder(p):
    global preorder_ans
    if p != '.':
        preorder_ans += p
        preorder(d[p][0])
        preorder(d[p][1])


def inorder(p):
    global inorder_ans
    if p != '.':
        inorder(d[p][0])
        inorder_ans += p
        inorder(d[p][1])


def postorder(p):
    global postorder_ans
    if p != '.':
        postorder(d[p][0])
        postorder(d[p][1])
        postorder_ans += p


def solution():
    global preorder_ans, inorder_ans, postorder_ans
    n = int(sys.stdin.readline().rstrip())
    for i in range(n):
        p, l_s, r_s = map(str, sys.stdin.readline().rstrip().split())
        d[p] = [l_s, r_s]
    preorder('A')
    inorder('A')
    postorder('A')
    print(preorder_ans)
    print(inorder_ans)
    print(postorder_ans)


if __name__ == "__main__":
    solution()