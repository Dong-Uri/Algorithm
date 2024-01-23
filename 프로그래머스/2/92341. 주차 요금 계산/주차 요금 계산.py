def all_time(in_time, out_time):
    in_h, in_m = map(int, in_time.split(':'))
    out_h, out_m = map(int, out_time.split(':'))
    m = (out_h - in_h) * 60 + out_m - in_m
    return m

def fee(m, fees):
    if m <= fees[0]:
        return fees[1]
    else:
        return fees[1] + ((m - fees[0] - 1) // fees[2] + 1) * fees[3]

def solution(fees, records):
    car_info = {} # 차랑번호 : [누적시간, 입차시간, 입차상태]
    for record in records:
        time, car, inout = record.split()
        if inout == 'OUT':
            car_info[car][0] += all_time(car_info[car][1], time)
            car_info[car][2] = 0
        elif car in car_info.keys():
            car_info[car][1] = time
            car_info[car][2] = 1
        else:
            car_info[car] = [0, time, 1]
    answer = []
    for car, info in sorted(car_info.items()):
        if info[2]:
            info[0] += all_time(info[1], '23:59')
        answer.append(fee(info[0], fees))
    return answer