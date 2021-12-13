from collections import deque


def calc_cost(cur_dir, nex_dir, cost):
    if (cur_dir == 'R' or cur_dir == 'L') and (nex_dir == 'L' or nex_dir == 'R'):
        return cost + 100
    if (cur_dir == 'D' or cur_dir == 'U') and (nex_dir == 'D' or nex_dir == 'U'):
        return cost + 100
    if (cur_dir == 'R' or cur_dir == 'L') and (nex_dir == 'D' or nex_dir == 'U'):
        return cost + 600
    if (cur_dir == 'D' or cur_dir == 'U') and (nex_dir == 'R' or nex_dir == 'L'):
        return cost + 600


def bfs(x, y, cost, direct):
    queue = deque([(x, y, cost, direct)])
    check = [[0 for _ in range(N)] for _ in range(N)]
    check[x][y] = 1
    while queue:
        x, y, cost, cur_dir = queue.popleft()
        if x == N - 1 and y == N - 1:
            answer.append(cost)
            continue
        for i, j, d in (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U'):
            nx, ny, new_cost = x + i, y + j, calc_cost(cur_dir, d, cost)
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if not new_board[nx][ny]:
                if not check[nx][ny] or check[nx][ny] > new_cost:
                    check[nx][ny] = new_cost
                    queue.append((nx, ny, new_cost, d))


def solution(board):
    global N, check, new_board, answer
    answer = []
    N = len(board)
    new_board = [board[i][:] for i in range(N)]
    bfs(0, 0, 0, 'R')
    bfs(0, 0, 0, 'D')
    return min(answer)


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
board2 = [[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]
board3 = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
board4 = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0]]
sol = solution(board2)
print(sol)