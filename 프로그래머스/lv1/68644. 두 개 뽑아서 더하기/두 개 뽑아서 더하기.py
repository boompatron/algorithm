def solution(numbers):
    s = set()
    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            s.add(numbers[i] + numbers[j])
    for i in sorted(list(s)):
        answer.append(i)
    return answer