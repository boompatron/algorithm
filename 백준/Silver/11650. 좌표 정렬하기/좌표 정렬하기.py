n = int(input())
coord = [[0, 0] for i in range(n)]
for i in range(n):
    xpos, ypos = map(int, input().split())
    coord[i][0] = xpos
    coord[i][1] = ypos
l = sorted(coord, key=lambda x: (x[0], x[1]))
for i in range(len(l)):
    print(l[i][0], l[i][1], sep=" ")