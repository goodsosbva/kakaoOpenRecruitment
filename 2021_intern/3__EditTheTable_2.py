class Node:
    def __init__(self):
        self.remove = False
        self.prev = None
        self.next = None


def solution(n, k, cmd):
    nodearr = [Node() for _ in range(n)]

    # 연결리스트 이용
    for i in range(1, n):
        nodearr[i - 1].next = nodearr[i]
        nodearr[i].prev = nodearr[i - 1]

    cur = nodearr[k]
    tmp = []

    for c in cmd:
        if c[0] == 'U':
            x = int(c[2:])
            for _ in range(x):
                cur = cur.prev

        elif c[0] == 'D':
            x = int(c[2:])
            for _ in range(x):
                cur = cur.next
        elif c[0] == 'C':
            tmp.append(cur)
            cur.remove = True
            top = cur.prev
            bottom = cur.next
            # 첫 번재 행인 경우 고려
            if top:
                top.next = bottom
            # 마지막행인 경우 고려
            if bottom:
                bottom.prev = top
                cur = bottom
            # 삭제되는 행이 마지막 행인 경우
            else:
                cur = top
        else:  # str[0] == 'Z'
            node = tmp.pop()
            node.remove = False
            # prev, next 삭제하지 않았으니까 방향 값은 살아 있음.
            top = node.prev
            down = node.next
            if top:
                top.next = node
            if down:
                down.prev = node

    answer = ''
    for i in range(n):
        if nodearr[i].remove:
            answer += 'X'
        else:
            answer += 'O'
    return answer


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
sol = solution(n, k, cmd)
print(sol)