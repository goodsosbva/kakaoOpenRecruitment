import sys
# 원리는 2번째 풀이와 같음, 그저 반복문 대신 재귀를 썼을 뿐
sys.setrecursionlimit(10000)  # 재귀 허용깊이 임의로 지정


def solution(k, room_number):
    rooms = dict()  # {방번호: 바로 다음 빈방 번호}
    for num in room_number:
        chk_in = find_empty_room(num, rooms)
    return list(rooms.keys())


def find_empty_room(chk, rooms):  # 재귀함수
    if chk not in rooms.keys():  # 빈 방이면
        rooms[chk] = chk + 1  # rooms 새 노드 추가
        return chk  # 요청한 방
    empty = find_empty_room(rooms[chk], rooms)  # 재귀함수 호출
    rooms[chk] = empty + 1  # (배정된 방 + 1)을 부모노드로 변경
    return empty  # 새로 찾은 빈 방


# 답 : [1,3,4,2,5,6]
k = 10
room_number = [1, 3, 4, 1, 3, 1]
sol = solution(k, room_number)
print(sol)
