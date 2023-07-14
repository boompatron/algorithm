def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3)
    return str(int(''.join(reversed(numbers))))