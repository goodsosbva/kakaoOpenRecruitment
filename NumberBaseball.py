# 숫자 야구
import random

global gStrikeCount
global gBallCount
global gTryCount
global answer_nums
answer_nums = [0, 0, 0]
max_count = 9
gStrikeCount = 0
gBallCount = 0
gTryCount = 0


# set answer
def setanswer():
    global answer_nums
    while True:
        randnum = int(random.random() * 10000 % 1000)
        answer_nums[2] = randnum % 10
        answer_nums[0] = int(randnum / 100)
        answer_nums[1] = int(randnum % 100 / 10)
        if isValidNum(answer_nums):
            break
    return answer_nums

# check valid
# dup check & check zero
def isValidNum(inputstr):
    flag = True
    # if inputstr[0].isdecimal() != True and inputstr[1].isdecimal() != True and inputstr[2].isdecimal() != True:
    #    print("Number is only!")
    #    flag = False
    if len(inputstr) != 3:
        print("input the 3 length!")
        flag = False
    elif hasDumpNumberAndZero(inputstr) != True:
        print("do not input duplicated num or zero!")
        flag = False

    if flag == False:
        return False

    return True


def hasDumpNumberAndZero(val):
    if val[0] == 0 or val[1] == 0 or val[2] == 0:
        return False
    if val[0] == val[1] or val[1] == val[2] or val[0] == val[2]:
        return False

    return True


# question
def printQuestion():
    return print("input the 3 num")

def endgame():
    if gStrikeCount == 3: print("you win!")
    else: print("you fail")

    print("See you next time~")
    return

def resetgame():
    global gStrikeCount
    global gBallCount
    global gTryCount
    gStrikeCount = 0
    gBallCount = 0
    gTryCount = 0
    print("New Game start!")
    printQuestion()
    setanswer()
    return




setanswer()
# answer_nums = [2, 7, 4]
# readline
while True:
    term = input()
    if term == "q":
        endgame()
        break
    if term == "r":
        resetgame()
        continue

    if not isValidNum(term):
        printQuestion()
        continue

    for i in range(len(answer_nums)):
        if int(term[i]) in answer_nums:
            if int(term[i]) == answer_nums[i]:
                gStrikeCount += 1
            else: gBallCount += 1
    print("\n[", gStrikeCount, "] 스트라이크! [", gBallCount, "] 볼!\n")
    print("정답: ", answer_nums)
    print("남은 기회: ", max_count - gTryCount - 1)

    gTryCount += 1

    if gStrikeCount == 3 or gTryCount > max_count:
        endgame()
        break
    else:
        gStrikeCount = 0
        gBallCount = 0


# end game with score(win or fail)
