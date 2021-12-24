# 4. 미로 탈출
import queue
INF = 99999


def dij(n, graph, src, dst, traps):
    prior_q = queue.PriorityQueue()
    visited = [[False for _ in range(1 << len(traps))] for _ in range(n + 1)]
    prior_q.put((0, src, 0))

    while not prior_q.empty():
        cur = prior_q.get()
        w = cur[0]
        u = cur[1]
        state = cur[2]

        if u == dst:
            return w
        if visited[u][state]:
            continue
        visited[u][state] = True

        # 이동 노드와 현재 노드의 함정 여부를 체크 해주어야함함
        curTrap = False
        trapped = {}
        # 함정 목록에 있는 인덱스에 따라서 비트를 설정
        for i in range(len(traps)):
            bit = 1 << i
            # 0이 아니면 해당 함정이 발동 되있는 상태
            if state & bit:
                # 함정이 발동된 곳을 다시 온 경우
                if traps[i] == u:
                    state &= ~bit
                else:
                    trapped[traps[i]] = True
            # 발동된 상태는 아니지만
            else:
                # 함정 노드로 온 경우
                if traps[i] == u:
                    state |= bit
                    trapped[traps[i]] = True
                    curTrap = True

        for v in range(1, n + 1):
            if v == u:
                continue
            nextTrap = True if v in trapped else False
            if curTrap == nextTrap:
                if graph[u][v] != INF:
                    prior_q.put((w + graph[u][v], v, state))
            else:
                if graph[v][u] != INF:
                    prior_q.put((w + graph[v][u], v, state))
    return INF


def solution(n, start, end, roads, traps):
    # 인덱스 0은 안쓸것
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    # 자기 자신의 거리는 0
    for i in range(1, n + 1):
        graph[i][i] = 0

    for d in roads:
        u, v, w = d[0], d[1], d[2]
        # 가장 작은 인접행열만 필요하기 때문에 작은값만 기억
        if w < graph[u][v]:
            graph[u][v] = w

    return dij(n, graph, start, end, traps)


n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
sol = solution(n, start, end, roads, traps)
print(sol)