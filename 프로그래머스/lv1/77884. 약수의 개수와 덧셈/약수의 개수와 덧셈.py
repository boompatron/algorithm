def solution(left, right):
    answer = 0
    is_plus = [False for _ in range(right + 1)]
    for i in range(left, right + 1):
        div = 0
        for j in range(1, i + 1):
            if i % j == 0:
                div += 1
        if div % 2 == 0:
            is_plus[i] = True
    for i in range(left, right + 1):
        answer += i if is_plus[i] else -i
    return answer