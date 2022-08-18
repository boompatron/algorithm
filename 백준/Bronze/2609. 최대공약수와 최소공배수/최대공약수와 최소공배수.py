a, b = map(int, input().split())
a_list = []; b_list = []
a_measure = {}; b_measure = {}
LCM = {}; GCF = {}
while a > 1:
    for i in range(2, a + 1):
        if a % i == 0:
            a_list.append(i)
            if i in a_measure:
                a_measure[i] += 1
            else:
                a_measure[i] = 1
            a //= i
            break
while b > 1:
    for i in range(2, b + 1):
        if b % i == 0:
            b_list.append(i)
            if i in b_measure:
                b_measure[i] += 1
            else:
                b_measure[i] = 1
            b //= i
            break

a_list = list(a_measure.keys())
b_list = list(b_measure.keys())

for i in range(len(a_list)):
    for j in range(len(b_list)):
        if a_list[i] == b_list[j]:
            if a_measure[a_list[i]] > b_measure[b_list[j]]:
                GCF[b_list[j]] = b_measure[b_list[j]]
            else :
                GCF[a_list[i]] = a_measure[a_list[i]]

for i in range(len(a_list)):
    LCM[a_list[i]] = a_measure[a_list[i]]

for j in range(len(b_list)):
    if b_list[j] in LCM and LCM[b_list[j]] < b_measure[b_list[j]]:
        LCM[b_list[j]] = b_measure[b_list[j]]
    elif not b_list[j] in LCM:
        LCM[b_list[j]] = b_measure[b_list[j]]

if not len(GCF.keys()):
    GCF[1] = 1
gcf = 1
for key in GCF.keys():
    gcf *= key ** GCF[key]
lcm = 1
for key in LCM.keys():
    lcm *= key ** LCM[key]
print(gcf)
print(lcm)
