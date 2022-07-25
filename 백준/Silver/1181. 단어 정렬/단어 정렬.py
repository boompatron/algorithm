n = int(input())
s_list = ["" for i in range(n)]
for i in range(n):
    s = input()
    s_list[i] = s
s_list = list(set(s_list))
l = sorted(s_list, key=lambda x: (len(x), x))
for i in l:
    print(i)