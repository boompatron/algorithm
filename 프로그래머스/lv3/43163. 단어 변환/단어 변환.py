from collections import deque


def is_nearby(str1, str2):
    cnt = 0
    for s1, s2 in zip(str1, str2):
        if s1 != s2:
            cnt += 1
    return True if cnt == 1 else False


def solution(begin, target, words):
    n = len(words)
    d = {}
    for w in words:
        d[w] = []
    for i in range(n):
        for j in range(i, n):
            if is_nearby(words[i], words[j]):
                d[words[i]].append(words[j])
                d[words[j]].append(words[i])
    dq = deque()
    for w in words:
        if is_nearby(begin, w):
            dq.appendleft([w, 0])
    while dq:
        word, cnt = dq.pop()
        if word == target:
            return cnt + 1
        if cnt > n:
            break
        for next_word in d[word]:
            dq.appendleft([next_word, cnt + 1])
    return 0