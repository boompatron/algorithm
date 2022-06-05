alpha = [0 for i in range(26)]
a = input()
a = a.upper()
for i in range(len(a)):
    alpha[ord(a[i]) - 65] += 1;
ans = 0
for i in range(26):
    if alpha[i] > alpha[ans]:
        ans = i
overlap = False
for i in range(26):
    if alpha[ans] == alpha[i] and i != ans:
        overlap = True

if overlap:
    print("?")
else:
    print(chr(ans + 65))