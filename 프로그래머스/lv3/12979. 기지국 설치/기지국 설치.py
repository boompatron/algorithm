def solution(n, stations, w):
    sn = len(stations)
    ans, si, pos = 0, 0, 1
    while pos <= n:
        if si < sn and stations[si] - w <= pos:
            pos = stations[si] + w + 1
            si += 1
        else:
            ans += 1
            pos += 2 * w + 1
    return ans