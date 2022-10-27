import sys
from collections import deque


def main():
    v = int(sys.stdin.readline().rstrip())
    a, b = map(int, sys.stdin.readline().rstrip().split())
    e = int(sys.stdin.readline().rstrip())
    adj, cnt = [[] for _ in range(v + 1)], [1e7 for _ in range(v + 1)]
    cnt[a] = 0
    for _ in range(e):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        adj[v1].append(v2)
        adj[v2].append(v1)

    def bfs(person: int):
        dq = deque()
        dq.appendleft((person, 0))
        while dq:
            cur, rel = dq.pop()
            for next_person in adj[cur]:
                if next_person == b:
                    return rel + 1
                if cnt[next_person] > rel + 1:
                    dq.appendleft((next_person, rel + 1))
                    cnt[next_person] = rel + 1
        return 1e7
    ans = bfs(a)
    print(ans if ans != 1e7 else -1)


if __name__ == '__main__':
    main()
