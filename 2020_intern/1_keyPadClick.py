# 1. 키 패드 누르기


def solution(numbers, hand):
    keyPad = \
    {
     1: (0, 0), 2: (0, 1), 3: (0, 2),
     4: (1, 0), 5: (1, 1), 6: (1, 2),
     7: (2, 0), 8: (2, 1), 9: (2, 2),
     "*": (3, 0), 0: (3, 1), "#": (3, 2),
    }
    handPosition = ["*", "#"]
    leftKey = [1, 4, 7]
    rightKey = [3, 6, 9]

    answer = ''
    for n in numbers:
        if n in leftKey:
            answer += 'l'
            # 현재 위치 최신화
            handPosition[0] = n
        elif n in rightKey:
            answer += 'r'
            # 현재 위치 최신화
            handPosition[1] = n
        else:  # 더 가까운 쪽으로 접근하게
            nearHand = getNearHand(keyPad, handPosition[0], handPosition[1], n, hand)
            if nearHand == 'l':
                answer += 'l'
                # 현재 위치 최신화
                handPosition[0] = n
            else:
                answer += 'r'
                # 현재 위치 최신화
                handPosition[1] = n


    return answer.upper()


def getNearHand(keyPad, l, r, n, hand):
    # x, y 좌표 빼주기
    # 왼쪽 거리
    leftDistance = abs(keyPad[l][0] - keyPad[n][0]) + \
                   abs(keyPad[l][1] - keyPad[n][1])

    # 오른쪽 거리
    rightDistance = abs(keyPad[r][0] - keyPad[n][0]) + \
                   abs(keyPad[r][1] - keyPad[n][1])

    if leftDistance == rightDistance:
        nearHand = 'l' if hand == "left" else "r"
    else:
        nearHand = 'l' if leftDistance < rightDistance else 'r'
    return nearHand


# 결과 	"LRLLLRLLRRL"
hand = "right"
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
sol = solution(numbers, hand)
print(sol)