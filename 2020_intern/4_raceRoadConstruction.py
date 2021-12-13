# 4. 경주로 건설

"""
이때, 인접한 두 빈 칸을 상하 또는 좌우로 연결한 경주로를 직선 도로 라고 합니다.
또한 두 직선 도로가 서로 직각으로 만나는 지점을 코너 라고 부릅니다.
건설 비용을 계산해 보니 직선 도로 하나를 만들 때는 100원이 소요되며, 코너를 하나 만들 때는 500원이 추가로 듭니다.
죠르디는 견적서 작성을 위해 경주로를 건설하는 데 필요한 최소 비용을 계산해야 합니다.
"""

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def cal(sol):
    # 값 계산
    l = True
    r = True
    sum = 0
    for i in range(len(sol) - 1):
        # print(sol[i][1], sol[i][0],l, r, sum, end=" ")
        if (sol[i][0] + 1 == sol[i + 1][0]) and l == True:
            # print("1")
            l = True
            r = False
            sum += 100

        elif (sol[i][1] + 1 == sol[i + 1][1]) and r == True:
            # print("2")
            l = False
            r = True
            sum += 100

        elif (sol[i][0] + 1 == sol[i + 1][0]) and l == False:
            # print("3")
            l = True
            r = True
            sum += 600
        elif (sol[i][1] + 1 == sol[i + 1][1]) and r == False:
            # print("4")
            l = True
            r = True
            sum += 600

    return sum


def FindLoad(maze, x, y, foots):
    n = len(maze)
    foot = maze[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if nx == n - 1 and ny == n - 1:
                maze[nx][ny] = foot + 1
                foots.append([nx, ny])
                return True
            if maze[nx][ny] == 0:
                maze[nx][ny] = foot + 1
                if FindLoad(maze, nx, ny, foots):
                    foots.append([nx, ny])
                    return True


def solution(maze):
    x, y = 0, 0
    foots = []
    FindLoad(maze, x, y, foots)
    foots.append([0, 0])
    foots.reverse()

    # print(foots)
    answer = cal(foots)
    return answer


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board2 = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
board3 = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
board4 = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0]]
sol = solution(board2)
print(sol)
