a, b = map(int, input().split())
new_a = new_b = 0
while b > 0:
    new_b *= 10
    new_b += b % 10
    b //= 10
while a > 0:
    new_a *= 10
    new_a += a % 10
    a //= 10
if new_a > new_b:
    print(new_a)
else:
    print(new_b)