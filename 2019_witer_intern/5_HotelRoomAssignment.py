# 5. 호텔 방 배정 문제
from collections import deque


def solution(k, room_number):
    room_number = deque(room_number)

    answer = []
    dp = [0] * (k + 1)

    while room_number:
        # print(dp)
        n = room_number.popleft()
        if dp[n] != 0:
            tmp = n
            while True:
                if dp[tmp] != 0:
                    tmp += 1
                else:
                    dp[tmp] = tmp
                    answer.append(tmp)
                    break
        else:
            dp[n] = n
            answer.append(n)

    # print(dp)
    # print(answer)
    return answer


# 답 : [1,3,4,2,5,6]
k = 10
room_number = [1, 3, 4, 1, 3, 1]
sol = solution(k, room_number)
print(sol)
