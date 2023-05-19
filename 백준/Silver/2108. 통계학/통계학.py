import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
g = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
g.sort()
print(round(sum(g) / n))
print(g[n // 2])
d = defaultdict(int)
for i in g:
    d[i] += 1
most_appeared = []
for key in d.keys():
    if d[key] == max(d.values()):
        most_appeared.append(key)
most_appeared.sort()
print(most_appeared[0] if len(most_appeared) == 1 else most_appeared[1])
print(g[-1] - g[0])
