while True:
    stack = []
    queue = []
    pellin = list(input())
    isPellin = True
    if pellin[0] == '0':
        break
    else:
        stack = pellin
        queue = pellin

        for i in range(len(pellin)):
            if stack[i] != queue[len(pellin) - 1 - i]:
                isPellin = False
        if isPellin:
            print("yes")
        else:
            print("no")