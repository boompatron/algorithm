g = list(map(ord, input()))
for i in range(len(g)):
    if 65 <= g[i] <= 90:
        g[i] += 32
    else:
        g[i] -= 32
print(''.join(map(chr, g)))