a = int(input())
while a:
    l = list(input())
    num = int(l[0])
    l = l[2:]
    #print("size : " , num, "list : " , l)
    for i in range(len(l)):
        for j in range(num):
            print(l[i], end="")
    print()
    a -= 1