ans = 0; cnt = 0
for i in range(9):
    a = int(input())
    if ans < a:
        cnt = i + 1
        ans = a
print(ans)
print(cnt)