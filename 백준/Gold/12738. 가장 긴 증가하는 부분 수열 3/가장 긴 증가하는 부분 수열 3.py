import sys

n = int(sys.stdin.readline().rstrip())
g = list(map(int, sys.stdin.readline().rstrip().split()))

ans = [-sys.maxsize]
for cur in g:
    if ans[-1] < cur:
        ans.append(cur)
    else:
        left = 0
        right = len(ans)

        while left < right:
            mid = (right + left) // 2
            if ans[mid] < cur:
                left = mid + 1
            else:
                right = mid
        ans[right] = cur
print(len(ans) - 1)
