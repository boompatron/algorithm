discount_rate = (10, 20, 30, 40)
ans = [0, 0]


def solution(users, emoticons):
    global ans
    n = len(emoticons)

    def dfs(discount_info: list):
        if len(discount_info) == n:
            tmp = [0, 0]
            for lower_discount_rate, upper_amount in users:
                amount = 0
                for i in range(n):
                    if discount_info[i] >= lower_discount_rate:
                        amount += int((100 - discount_info[i]) * emoticons[i] / 100)
                if amount >= upper_amount:
                    tmp[0] += 1
                else:
                    tmp[1] += amount
            global ans
            if tmp[0] > ans[0] or (tmp[0] == ans[0] and tmp[1] > ans[1]):
                ans = tmp
            return
        for rate in discount_rate:
            discount_info.append(rate)
            dfs(discount_info)
            discount_info.pop(-1)

    dfs([])
    return ans