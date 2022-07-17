def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    reported_cnt = {}
    reported_list = {}
    for i in id_list:
        reported_cnt[i] = 0
        reported_list[i] = set()
    for r in report:
        a, b = r.split()
        reported_cnt[b] += 0 if b in reported_list[a] else 1
        reported_list[a].add(b)
    for i in enumerate(id_list):
        for j in reported_list[i[1]]:
            if j in reported_cnt.keys() and reported_cnt[j] >= k:
                answer[i[0]] += 1
    return answer