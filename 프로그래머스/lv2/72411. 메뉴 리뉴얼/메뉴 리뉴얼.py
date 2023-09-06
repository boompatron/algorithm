from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    ans = []
    for num in course:
        candidate, dd = [], defaultdict(int)
        for order in orders:
            candidate.extend(list(combinations(sorted(order), num)))

        for can in candidate:
            order = ''.join(can)
            dd[order] += 1

        for k in dd.keys():
            if dd[k] == max([dd[kk] for kk in dd.keys()]):
                if dd[k] > 1:
                    ans.append(k)
    return sorted(ans)