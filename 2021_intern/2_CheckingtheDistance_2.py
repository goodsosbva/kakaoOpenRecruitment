# 거리두기 확인하기 풀이_2


def solution(places):
    result = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def DFS(x, y, cnt):
        nonlocal good
        if cnt > 2:
            return
        if 0 <= x < 5 and 0 <= y < 5:
            if graph[x][y] == 'X':
                return

            if cnt != 0 and graph[x][y] == 'P':
                good = 0
                return

            # 현재위치를 P로 착각하면 안되니까
            graph[x][y] = 'O'

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                DFS(nx, ny, cnt + 1)

    for case in places:
        graph = [list(r) for r in case]
        good = 1
        for x in range(5):
            for y in range(5):
                if graph[x][y] == 'P':
                    DFS(x, y, 0)

        result.append(good)
    return result


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
sol = solution(places)
print(sol)
