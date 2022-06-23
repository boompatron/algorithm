import sys

n = int(sys.stdin.readline())
price = [[0] for i in range(3)]
for i in range(n):
    r_tmp, g_tmp, b_tmp = map(int, sys.stdin.readline().split())
    price[0].append(r_tmp)
    price[1].append(g_tmp)
    price[2].append(b_tmp)
for i in range(1, n + 1):
    for j in range(3):
        tmp_minimum = 1234567
        for k in range(3):
            if j != k:
                if price[j][i] + price[k][i - 1] < tmp_minimum:
                    tmp_minimum = price[j][i] + price[k][i - 1]
        price[j][i] = tmp_minimum
ans = 1234567
for i in range(3):
    if price[i][n] < ans:
        ans = price[i][n]
print(ans)
