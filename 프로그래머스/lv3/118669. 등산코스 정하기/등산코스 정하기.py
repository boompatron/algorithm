import sys, heapq
INF = sys.maxsize


def solution(n, paths, gates, summits):
    adj = [[] for _ in range(n + 1)]
    for v1, v2, w in paths:
        adj[v1].append([v2, w])
        adj[v2].append([v1, w])

    summits.sort()
    _summits = set(summits)
    intensity = [INF for _ in range(n + 1)]

    def dijkstra():
        hq = []
        for gate in gates:
            heapq.heappush(hq, [0, gate])
            intensity[gate] = 0

        while hq:
            cur_intensity, node = heapq.heappop(hq)

            if node in _summits or intensity[node] < cur_intensity:
                continue

            for n_node, next_intensity in adj[node]:
                next_intensity = max(cur_intensity, next_intensity)
                if intensity[n_node] > next_intensity:
                    intensity[n_node] = next_intensity
                    heapq.heappush(hq, [next_intensity, n_node])
        ans = [n + 1, INF]
        for summit in reversed(summits):
            if ans[1] >= intensity[summit]:
                ans = [summit, intensity[summit]]
        return ans

    return dijkstra()