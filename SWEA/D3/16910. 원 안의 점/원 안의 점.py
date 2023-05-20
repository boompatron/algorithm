tc = int(input().rstrip())

for test_case in range(1, tc + 1):
    n = int(input().rstrip())
    m = n * n
    cnt = 0
    for x in range(-n, n + 1):
        for y in range(-n, n + 1):
            if x * x + y * y <= m:
                cnt += 1
    print(f'#{test_case} {cnt}')
