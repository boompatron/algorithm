import sys
import heapq


def dijkstra(start, ans_list, adj_list):
    ans_list[start] = 0
    hq = []
    heapq.heappush(hq, [0, start])
    while len(hq):
        dis, cur = heapq.heappop(hq)
        if ans_list[cur] < dis:
            # 현재 ans[cur]에 들어있는 값이 현재보다 더 작으므로 갱신할 필요가 없음 그래서 넘어감
            continue
        # 하지만 이제 더 작아서 갱신이 가능하다면
        # 그 점이랑 연결된 점들과의 거리르 비교해서 ans를 갱싱해야 함
        for a in adj_list[cur]: # 현재 점들과 연결된 점들을 search
            next_num, next_dis = a[0], a[1] + dis # 다음 점 위치와 다음 점 까지의 거리 : 지금가지의 거리(dis) + adj에 저장된 거리
            if next_dis < ans_list[next_num]: # 만약 ans에 저장된 값보다 더 작으면 수색할 가치가 있다고 판단, hq에 넣음
                ans_list[next_num] = next_dis # 값을 갱신함
                heapq.heappush(hq, [next_dis, next_num])


def solution():
    v, e = map(int, sys.stdin.readline().rstrip().split())
    adj, ans = [[] for _ in range(v + 1)], [123456789 for i in range(v + 1)]
    start_vertex = int(sys.stdin.readline().rstrip())
    for _ in range(e):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        adj[a].append([b, c])
    dijkstra(start_vertex, ans, adj)
    for i in range(1, v + 1):
        if ans[i] == 123456789:
            print("INF")
        else:
            print(ans[i])


if __name__ == "__main__":
    solution()
