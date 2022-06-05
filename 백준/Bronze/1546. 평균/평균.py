cnt = int(input()); M = 0; sum = 0
score = [0 for i in range(cnt)]
score = list(map(int, input().split()))
for i in range(cnt):
    if M < score[i]:
        M = score[i]
for i in range(cnt):
    score[i] = score[i] / M * 100
    sum += score[i]
print(sum / cnt)
