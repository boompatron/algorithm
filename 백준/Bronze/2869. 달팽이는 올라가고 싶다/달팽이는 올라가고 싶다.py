a, b, v = map(int, input().split())
(v - a) // (a - b)
if (v - a) % (a - b) == 0:
    print((v - a) // (a - b) + 1)
else:   #(v - a) % (a - b) != 0
    print((v - a) // (a - b) + 2)
