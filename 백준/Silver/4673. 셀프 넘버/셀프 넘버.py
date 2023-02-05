def d(a = int):
    sum = arg = a;
    while arg > 0:
        sum += arg % 10;
        arg //= 10;
    return sum;
self = [True for i in range(10001)]
for i in range(10000):
    if d(i + 1) < 10000:
        self[d(i + 1)] = False
for i in range(1, 10000):
    if self[i]:
        print(i)