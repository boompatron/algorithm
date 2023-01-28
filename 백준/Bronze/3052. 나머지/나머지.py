module_bool = [False for i in range(42)]
ans = 0
for i in range(10):
   a = int(input())
   module_bool[a % 42] = True
for i in range(42):
    if module_bool[i] :
        ans += 1
print(ans)
