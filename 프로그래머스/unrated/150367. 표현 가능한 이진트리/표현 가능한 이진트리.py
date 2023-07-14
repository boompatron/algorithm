def check_tree(tree):
    size = len(tree)
    if size == 1 or '1' not in tree or '0' not in tree:
        return True
    mid = size // 2
    if tree[mid] == '0':
        return False

    return check_tree(tree[:mid]) and check_tree(tree[mid + 1:])


def solution(numbers):
    ans = []
    for number in numbers:
        number = bin(number)[2:]
        tree_size = 1
        while tree_size < len(number):
            tree_size = (tree_size + 1) * 2 - 1
        number = '0' * (tree_size - len(number)) + number
        ans.append(1 if check_tree(number) else 0)
    return ans