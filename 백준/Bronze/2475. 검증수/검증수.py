num = list(map(int, input().split()))
sum = 0
for i in range(len(num)):
    sum += num[i]**2
print(sum % 10)