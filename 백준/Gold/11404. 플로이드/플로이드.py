import sys
INF = sys.maxsize


# 한 노드에서 다른 노드로 가는데 다른데를 경유해서 가는게 더 빠르다면 둘 사이의 거리를 갱신한다.
# 이게 플로이드 와샬, 그렇기 때문에 O(n ** 3)
# 다익스트라와는 다르게 모든 점에서 구해야 하기 때문에 DP보다는 그리디적인 성격이 있는듯...??
def floyd_warshall(ans, v):
    for k in range(1, v + 1):                       # 경유지 노드
        for i in range(1, v + 1):                   # 출발 노드
            for j in range(1, v + 1):               # 도착 노드
                if ans[i][k] + ans[k][j] < ans[i][j]:
                    ans[i][j] = ans[i][k] + ans[k][j]


def print_mat(mat, v):
    for i in range(1, v + 1):
        for j in range(1,  v + 1):
            if mat[i][j] == INF:
                print(0, end=" ")
            else:
                print(mat[i][j], end=" ")
        print()


def solution():
    v = int(sys.stdin.readline().rstrip())
    e = int(sys.stdin.readline().rstrip())
    adj = [[INF for _ in range(v + 1)] for __ in range(v + 1)]
    for i in range(e):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        adj[a][b] = min(adj[a][b], c)
    for i in range(v + 1):
        adj[i][i] = 0
    floyd_warshall(adj, v)
    print_mat(adj, v)


if __name__ == "__main__":
    solution()
