import sys
from copy import deepcopy
dxs = (-1, 0, 1)


n = int(sys.stdin.readline().rstrip())
min_g = list(map(int, sys.stdin.readline().rstrip().split()))
max_g = deepcopy(min_g)
for i in range(1, n):
    tmp_max, tmp_min = [0 for _ in range(3)], [0 for _ in range(3)]
    cur = list(map(int, sys.stdin.readline().rstrip().split()))
    for x in range(3):
        max_tmp, min_tmp = 0, sys.maxsize
        for dx in dxs:
            nx = x + dx
            if 0 <= nx < 3:
                if min_g[nx] < min_tmp:
                    min_tmp = min_g[nx]
                if max_g[nx] > max_tmp:
                    max_tmp = max_g[nx]
        tmp_max[x] = cur[x] + max_tmp
        tmp_min[x] = cur[x] + min_tmp
    max_g = deepcopy(tmp_max)
    min_g = deepcopy(tmp_min)
print(max(max_g), min(min_g), sep=' ')
