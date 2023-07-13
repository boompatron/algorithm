def solution(today, terms, privacies):
    ans = []
    policy = {}

    def to_day(year, month, day):
        return year * 12 * 28 + month * 28 + day

    today = to_day(*map(int, today.split('.')))
    for term in terms:
        name, mm = term.split()
        policy[name] = int(mm)

    for i, e in enumerate(privacies):
        validate_until, p = e.split()
        validate_until = to_day(*map(int, validate_until.split('.'))) + policy[p] * 28
        if validate_until <= today:
            ans.append(i + 1)
    return ans