erasto = [True for i in range(123456 * 2 + 1)]
erasto[1] = False
pos = 2
while pos != 2 * 123456 + 1:
    if erasto[pos]:
        for i in range(2, (2 * 123456) // pos + 1):
            erasto[pos * i] = False
    pos += 1
while True:
    n = int(input())
    if n == 0:
        break
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if erasto[i]:
            cnt += 1
    print(cnt)