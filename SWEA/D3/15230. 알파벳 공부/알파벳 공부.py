correct = 'abcdefghijklmnopqrstuvwxyz'
n = int(input().rstrip())
for i in range(1, n + 1):
    cnt = 0
    evaluate = input().rstrip()
    for c, e in zip(correct, evaluate):
        if c == e:
            cnt += 1
        else:
            break
    print(f'#{i} {cnt}')
    