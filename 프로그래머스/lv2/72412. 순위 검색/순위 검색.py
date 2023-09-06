from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    ans, dd = [], defaultdict(list)
    for i in info:
        i = i.split()
        cond = i[:-1]
        score = int(i[-1])
        for j in range(5):
            case = list(combinations([0, 1, 2, 3], j))
            for c in case:
                tmp = cond[:]
                for k in c:
                    tmp[k] = '-'
                key = ''.join(tmp)
                dd[key].append(score)
    for value in dd.values():
        value.sort()
    
    for q in query:
        q = q.replace('and', '').split()
        cond = ''.join(q[:-1])
        target = int(q[-1])
        cur = dd[cond]
        if cur:
            idx = bisect_left(cur, target)
            ans.append(len(cur) - idx)
        else:
            ans.append(0)

    return ans