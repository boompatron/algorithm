a = int(input())
b = int(input())
c = b
for i in range(3):
    print(a * (c % 10))
    c //= 10
print(a * b)
