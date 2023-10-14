next_pos = [[1], [2], [3], [4], [5],
            [6, 21], [7], [8], [9], [10],
            [11, 25], [12], [13], [14], [15],
            [16, 27], [17], [18], [19], [20],
            [32], [22], [23], [24], [30],
            [26], [24], [28], [29], [24],
            [31], [20], [32]]
scores = [0, 2, 4, 6, 8,
          10, 12, 14, 16, 18,
          20, 22, 24, 26, 28,
          30, 32, 34, 36, 38,
          40, 13, 16, 19, 25,
          22, 24, 28, 27, 26,
          30, 35, 0]

g = list(map(int, input().rstrip().split()))
ans = 0

def dfs(depth, score, pos):
    global ans
    if depth == 10:
        ans = max(ans, score)
        return

    for i in range(4):
        cur = pos[i]

        if len(next_pos[cur]) == 2:
            # 두 칸짜리  중간에 건너뛰어서 이동해야함
            cur = next_pos[cur][1]
        else:
            cur = next_pos[cur][0]

        for _ in range(1, g[depth]):
            cur = next_pos[cur][0]

        if cur == 32 or (cur < 32 and cur not in pos):
            tmp = pos[i]
            pos[i] = cur
            dfs(depth + 1, score + scores[cur], pos)
            pos[i] = tmp


dfs(0, 0, [0 for _ in range(4)])
print(ans)
