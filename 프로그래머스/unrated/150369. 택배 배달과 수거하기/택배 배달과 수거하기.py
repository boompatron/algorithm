def solution(cap, n, deliveries, pickups):
    cnt = 0
    del_pos, pick_pos = -1, -1
    for i in range(n - 1, -1, -1):
        if deliveries[i]:
            del_pos = i
            break
    for i in range(n - 1, -1, -1):
        if pickups[i]:
            pick_pos = i
            break
    while del_pos > -1 or pick_pos > -1:
        cnt += max(del_pos, pick_pos) * 2 + 2
        del_cap, pick_cap = cap, cap
        while del_cap and del_pos > -1:
            min_val = min(del_cap, deliveries[del_pos])
            del_cap -= min_val
            deliveries[del_pos] -= min_val
            if not deliveries[del_pos]:
                del_pos -= 1
        while pick_cap and pick_pos > -1:
            min_val = min(pick_cap, pickups[pick_pos])
            pick_cap -= min_val
            pickups[pick_pos] -= min_val
            if not pickups[pick_pos]:
                pick_pos -= 1

        while not deliveries[del_pos] and del_pos > -1:
            del_pos -= 1
        while not pickups[pick_pos] and pick_pos > -1:
            pick_pos -= 1
    return cnt