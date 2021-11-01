# 1. 크레인 인형 뽑기

# 같음 체크 함수
def sameDoll(basket):
    if len(basket) >= 2:
        if basket[-1] == basket[-2]:
            return True
    return False


# 인형 뽑기 함수
def DollDraw(number, board):
    for x in range(len(board)):
        if board[x][number] != 0:
            doll = board[x][number]
            board[x][number] = 0
            return doll


def solution(board, moves):
    answer = 0
    basket = []

    for i in range(len(moves)):
        tmp_y = moves.pop(0) - 1
        # print(tmp_y, board)
        doll = DollDraw(tmp_y, board)
        if doll == None:
            continue
        basket.append(doll)
        # print(basket)
        if sameDoll(basket):
            answer += 2
            basket.pop()
            basket.pop()
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

sol = solution(board, moves)
print("답: ", sol)
