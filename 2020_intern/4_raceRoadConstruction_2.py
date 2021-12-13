dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def cal(sol):
    # 값 계산
    l = 1
    r = 1
    sum = 0
    for i in range(len(sol) - 1):

        if (sol[i][0] - 1 == sol[i + 1][0] or sol[i][0] + 1 == sol[i + 1][0]) and l == 1 and r == 1:
            print("1", end=" //")
            print(i + 1, "st", sol[i], "l:", l, "r:", r, sum)
            l = 1
            r = 0
            sum += 100

        elif (sol[i][1] - 1 == sol[i + 1][1] or sol[i][1] + 1 == sol[i + 1][1]) and r == 1 and r == 1:
            print("2", end=" //")
            print(i + 1, "st", sol[i], "l:", l, "r:", r, sum)
            l = 0
            r = 1
            sum += 100

        elif (sol[i][0] - 1 == sol[i + 1][0] or sol[i][0] + 1 == sol[i + 1][0]) or (sol[i][1] - 1 == sol[i + 1][1] or sol[i][1] + 1 == sol[i + 1][1]) and l == 0 and r == 1:
            print("3", end=" //")
            print(i + 1, "st", sol[i], "l:", l, "r:", r, sum)
            l = 1
            r = 1
            sum += 600
        elif (sol[i][0] - 1 == sol[i + 1][0] or sol[i][0] + 1 == sol[i + 1][0]) or (sol[i][1] - 1 == sol[i + 1][1] or sol[i][1] + 1 == sol[i + 1][1]) and r == 0 and l == 1:
            print("4", end=" //")
            print(i + 1, "st", sol[i], "l:", l, "r:", r, sum)
            l = 1
            r = 1
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
                foots.append([nx, ny, foot + 1])
                return True
            if maze[nx][ny] == 0:
                maze[nx][ny] = foot + 1
                if FindLoad(maze, nx, ny, foots):
                    foots.append([nx, ny, foot + 1])
                    return True


def solution(maze):
    x, y = 0, 0
    foots = []
    FindLoad(maze, x, y, foots)
    foots.append([0, 0, 0])
    foots.reverse()
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