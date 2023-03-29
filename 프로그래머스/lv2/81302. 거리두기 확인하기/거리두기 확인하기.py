from collections import deque
dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)


def solution(places):
    answer = []
    for place in places:
        is_success = True
        participants = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    participants.append([j, i])
        dq = deque()
        for j, i in participants:
            dq.appendleft((j, i, 0))
            visited = [[False for _ in range(5)] for __ in range(5)]
            visited[i][j] = True
            while dq:
                x, y, dis = dq.pop()
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 5 and 0 <= ny < 5 and not visited[ny][nx]:
                        if place[ny][nx] == 'O':
                            dq.appendleft((nx, ny, dis + 1))
                            visited[ny][nx] = True
                        elif place[ny][nx] == 'P':
                            if dis + 1 <= 2:
                                is_success = False
        answer.append(1 if is_success else 0)
    return answer