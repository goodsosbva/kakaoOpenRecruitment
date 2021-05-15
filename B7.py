import datetime


def solution(lines: str) -> int:
    # 로그의 시작, 종료 시각 저장
    combined_logs = []
    for log in lines:
        logs = log.split(' ')
        timestamp = datetime.datetime.strptime(logs[0] + ' ' + logs[1], "%Y-%m-%d %H:%M:%S.%f").timestamp()
        combined_logs.append((timestamp, -1))
        combined_logs.append((timestamp - float(logs[2][:-1]) + 0.001, 1))

    accumulated = 0
    max_requests = 1
    combined_logs.sort(key=lambda x: x[0])
    print(combined_logs)
    for i, elem1 in enumerate(combined_logs):
        current = accumulated
        print(current)
        # print(i, elem1)

        # 1초 미만 윈도우 범위 요청 수 계산
        for elem2 in combined_logs[i:]:
            # print(elem2[0], elem2[1])
            if elem2[0] - elem1[0] > 0.999:
                break
            if elem2[1] > 0:
                current += elem2[1]
        max_requests = max(max_requests, current)
        # print(elem1, end=" ")
        accumulated += elem1[1]
        # print(accumulated, end=" ")
    
    return max_requests



logs = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 0.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s",

]

sol = solution(logs)
print()
print(sol)

# timeStr = '2018-07-28 12:11:32'
# Thistime = datetime.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S').timestamp()

# times = ["1234", "5678"]
# print(float(times[1][:-1]))