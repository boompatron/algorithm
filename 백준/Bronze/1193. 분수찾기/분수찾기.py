a = int(input())
i = 1
sum = 0
while True:
    sum += i
    if a <= sum:
        break
    i += 1
s = sum - a + 1
m = i + 1 - s
if i % 2 == 1:
    print("{0}/{1}".format(s, m))
else:
    print("{0}/{1}".format(m, s))