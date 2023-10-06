import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
g = deque(map(int, sys.stdin.readline().rstrip().split()))
robot_pos = deque([False for _ in range(n)])
cnt, turn = 0, 0


while cnt < k:
    # 1. 벨트가 로봇과 함께 회전한다
    g.rotate(1)  # 컨베이어 벨트를 회전시킨다

    robot_pos.rotate(1)  # 로봇의 위치도 이동
    robot_pos[-1] = False  # 내리는 위치의 로봇은 내려주기

    # 2. 가장 먼저 위에 올라간 로봇 부터 한 칸 앞으로 이동한다(가능하면)
    for i in range(n - 2, -1, -1):
        if g[i + 1] and not robot_pos[i + 1] and robot_pos[i]:
            robot_pos[i] = False
            robot_pos[i + 1] = True
            g[i + 1] -= 1
            if not g[i + 1]:
                cnt += 1
    robot_pos[-1] = False

    # 3. 올리는 위치에 로봇을 올릴 수 잇으면 로봇을 올린다.
    if g[0]:
        robot_pos[0] = True
        g[0] -= 1
        if g[0] == 0:
            cnt += 1
    turn += 1
print(turn)
