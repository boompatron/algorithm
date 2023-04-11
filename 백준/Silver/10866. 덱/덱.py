import sys
n = int(input())
dequeue = []
while n:
    instruction = str(sys.stdin.readline())
    if instruction[:3] == 'pus':        #push
        num = 0
        if instruction[5] == 'b':
            num = int(instruction[10:-1])
            dequeue.insert(0, num)
        elif instruction[5] == 'f':
            num = int(instruction[11:-1])
            dequeue.append(num)

    elif instruction[:3] == 'pop':
        if len(dequeue):
            if instruction[4] == 'f':
                print(dequeue.pop(len(dequeue) - 1))
            elif instruction[4] == 'b':
                print(dequeue.pop(0))
        else:
            print(-1)
    elif instruction[:3] == 'siz':
        print(len(dequeue))
    elif instruction[:3] == 'emp':
        if len(dequeue):
            print(0)
        else:
            print(1)
    elif instruction[:3] == 'fro':
        if len(dequeue):
            print(dequeue[len(dequeue) - 1])
        else:
            print(-1)
    elif instruction[:3] == 'bac':
        if len(dequeue):
            print(dequeue[0])
        else:
            print(-1)
    n -= 1