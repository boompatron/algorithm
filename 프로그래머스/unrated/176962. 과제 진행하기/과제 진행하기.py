import heapq


def solution(plans):
    plans.sort(key=lambda x: (x[1], x[2]))
    hq = []
    ans = []
    last_name, last_end_h, last_end_m = '', 0, 0   # subject, end_h, end_m
    for name, start_time, duration in plans:
        h, m = int(start_time[:2]), int(start_time[-2:])
        between_time = h * 60 + m - (last_end_h * 60 + last_end_m)
        if between_time < 0:
            heapq.heappush(hq, [-h, -m, last_name, -between_time])
        else:
            ans.append(last_name)
            while hq and between_time and (hq[0][3] > (-hq[0][0] - h) * 60 + (-hq[0][1] - m)):
                if between_time >= hq[0][3]:
                    between_time -= hq[0][3]
                    ans.append(hq[0][2])
                    heapq.heappop(hq)
                else:
                    hq[0][3] -= between_time
                    break
        last_name = name
        minutes = m + int(duration)
        last_end_h = h + minutes // 60
        last_end_m = minutes % 60
    ans.append(last_name)
    while hq:
        h, m, name, b_time = heapq.heappop(hq)
        ans.append(name)
        
    return ans[1:]
