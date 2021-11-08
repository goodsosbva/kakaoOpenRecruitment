# Lv4 2019 겨울 인턴십
# 호텔 방 배정

def solution(k, room_number):
    answer = []
    # 체크용 딕셔너리
    room = {}
    # 손님을 받으며 체크하자
    for num in room_number:
        # 딕셔너리에 확인 0이라면 배정이 안됬고, 다른값이 있다면 이미 배정되었다.
        # get에 값이 없다면 0 반환되도록 한것
        number = room.get(num, 0)
        print(room, num)
        if number:
            # number 은 다음 방 번호
            # 임시변수에 배정하려고 한 방번호를 넣어준다,
            temp = [num]
            # 반복문을 돌면서 빈방이 나올때까지 체크
            while True:
                index = number
                # 이동했던 위치를 이용하여 다시 이동
                number = room.get(number, 0)
                # 방이 비어있다면 방을 할당 = 0이 리턴 됬다면
                if not number:
                    # 정답에 추가해주고
                    answer.append(index)
                    # 딕셔너리에 값을 등록하고
                    room[index] = index + 1
                    # 이전에 거쳤던 방들의 다음 방 번호 최신화 해준다.
                    print("temp: ", temp, index)
                    for i in temp:
                        room[i] = index + 1
                    break
                temp.append(number)
        # 배정이 안되어있다면 결과추가하고 방배정 되었다고 딕셔너리에 표시
        else:
            answer.append(num)
            room[num] = num + 1
    print(room)
    return answer


# 답 : [1,3,4,2,5,6]
k = 10
room_number = [1, 3, 4, 1, 3, 1]
sol = solution(k, room_number)
print(sol)
