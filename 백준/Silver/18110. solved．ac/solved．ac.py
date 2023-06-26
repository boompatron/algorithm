import sys
input = sys.stdin.readline
 
def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)
 
n = int(input())
if not n:
    print(0)
else:
    score = [int(input()) for _ in range(n)]
    trunc = round2(n * 0.15)
    apply_trunc = sorted(score)[trunc: n - trunc]
    average = round2(sum(apply_trunc) / len(apply_trunc))
    print(average)
    