def check_tree(tree):
    size = len(tree)
    mid = size // 2
    
    if size == 1 or '1' not in tree or '0' not in tree:
        return True
    # 리프 노드 이거나, 서브트리가 1111, 0000 이면 조건을 해당 서브트리는 더 이상 안봐도 됨
    if tree[mid] == '0':
        return False
    # 만약 서브트리의 최상위 부모노드가 0이면 안됨!!

    return check_tree(tree[:mid]) and check_tree(tree[mid + 1:])
    # 위 조건들 중 하나도 안걸리면 양 옆으로 트리를 나눠서 살펴봄
    # 분할 정복

    
    

def solution(numbers):
    ans = []
    for number in numbers:
        # 각 숫자들을 1차적으로 2진수로 변환
        number = bin(number)[2:]
        tree_size = 1
        while tree_size < len(number):
            tree_size = (tree_size + 1) * 2 - 1
        # 포화 이진트리에 넣기 위해 사이즈를 맞춰줌
        # 포화 이진트리는 2 ** n - 1
        # 부족한 노드는 0으로 앞에 채워야 이진수의 실제 값에 변경을 주지 않음
        number = '0' * (tree_size - len(number)) + number
        ans.append(1 if check_tree(number) else 0)
    return ans

