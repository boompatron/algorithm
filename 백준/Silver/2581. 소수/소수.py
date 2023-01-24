#m, n = map(int, input().split())
m = int(input())
n = int(input())
erasto = [True for i in range(n + 1)]
erasto[1] = False
pos = 2
while pos != n + 1:
    if erasto[pos]:
        for i in range(2, n // pos + 1):
            erasto[pos * i] = False
    pos += 1
sum = 0; min = -1
for i in range(m, n + 1):
    if erasto[i]:
        sum += i
        if min == -1:
            min = i
if sum > 0:
    print(sum)
print(min)