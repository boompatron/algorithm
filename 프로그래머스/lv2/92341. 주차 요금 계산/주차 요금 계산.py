from collections import defaultdict


def cal_time(in_time, out_time):
    ih, im = map(int, in_time.split(":"))
    oh, om = map(int, out_time.split(":"))
    return oh * 60 + om - (ih * 60 + im)


def cal_fee(fees, total_time):
    if total_time <= fees[0]:
        return fees[1]
    over_time = total_time - fees[0]
    total_fee = over_time // fees[2] * fees[3] if over_time % fees[2] == 0 else (over_time // fees[2] + 1) * fees[3]
    return total_fee + fees[1]


def solution(fees, records):
    cars = dict()
    accum_time = defaultdict(int)
    answer = []
    # print(fees)
    for record in records:
        tt, num, is_in = record.split()
        if is_in == 'IN':
            cars[num] = tt
        else:
            total_time = cal_time(cars[num], tt)
            cars[num] = ''
            accum_time[num] += total_time

    for car in cars.keys():
        if cars[car] != '':
            accum_time[car] += cal_time(cars[car], '23:59')
    for key in sorted(accum_time.keys()):
        # print(f'{key} : {accum_time[key]}')
        answer.append(cal_fee(fees, accum_time[key]))

    return answer
