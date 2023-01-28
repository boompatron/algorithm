num = list(map(int, input().split()))
asc  = dec = False
for i in range(len(num) - 1):
    if num[i] > num[i + 1]:
        dec = True
    else:
        asc = True
if asc and dec:
    print("mixed")
elif asc:
    print("ascending")
else:
    print("descending")