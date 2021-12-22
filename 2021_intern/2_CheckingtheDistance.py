# 2. 거리두기 확인하기

dx1 = [0, 1, 0, -1]
dy1 = [-1, 0, 1, 0]

dx2 = [1, -1, 1, -1]
dy2 = [1, 1, -1, -1]


def chkDistance(places, st, x, y):
    # 1칸 체크
    for i in range(4):
        nx = x + dx1[i]
        ny = y + dy1[i]
        if 0 <= nx < 5 and 0 <= ny < 5 and places[st][nx][ny] == 'P':
            return False

    # 대각선에 위치한 응시자 확인
    for dir in range(4):
        nx, ny = x + dx2[dir], y + dy2[dir]
        # 대각선에 응시자가 있을 경우 파티션 존재 여부 확인
        if 0 <= nx < 5 and 0 <= ny < 5 and places[st][nx][ny] == 'P':
            if places[st][x][ny] != 'X' or places[st][nx][y] != 'X':
                return False
    # 상하좌우로 거리가 2인 응시자 확인
    for dir in range(4):
        nx, ny = x + 2 * dx1[dir], y + 2 * dy1[dir]
        # 거리가 2인 곳에 응시자가 있을 경우 파티션 존재 여부 확인
        if 0 <= nx < 5 and 0 <= ny < 5 and places[st][nx][ny] == 'P':
            if places[st][x + dx1[dir]][y + dy1[dir]] != 'X':
                return False
    return True


def solution(places):
    answer = []
    row = len(places[0][0])
    col = len(places[0])
    flag = 1

    for i in range(len(places)):
        for x in range(row):
            for y in range(col):
                # print(places[i][x][y], end=" ")
                if places[i][x][y] != 'P':
                    continue
                if not chkDistance(places, i, x, y):
                    answer.append(0)
                    flag = 0
                    break
            if flag == 0:
                flag = 1
                break
            elif flag == 1 and x == 4 and y == 4:
                answer.append(1)
                break
            # print()
        # print("answer:", answer)
    # print(answer)
    return answer


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
sol = solution(places)
print(sol)
