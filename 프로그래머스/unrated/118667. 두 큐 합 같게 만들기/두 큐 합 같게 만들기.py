from collections import deque


def solution(queue1, queue2):
    dq1, dq2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(dq1), sum(dq2)
    cnt = 0
    for i in range(len(queue1) * 3):
        if sum1 == sum2:
            return cnt
        elif sum1 > sum2:
            tmp = dq1.popleft()
            dq2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        else:
            tmp = dq2.popleft()
            dq1.append(tmp)
            sum2 -= tmp
            sum1 += tmp
        cnt += 1
    return -1