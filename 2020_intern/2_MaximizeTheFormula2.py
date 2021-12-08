# 수식 최대화
import re


def Maximize(operator, expr):
    for op in operator:
        while op in expr:
            print(expr)
            idx = expr.index(op)
            expr[idx - 1] = str(eval(expr[idx - 1] + op + expr[idx + 1]))
            del expr[idx: idx + 2]

    return abs(int(expr[0]))


def solution(expression):
    op1 = ['-', '+', '*']
    op2 = ['+', '*', '-']
    op3 = ['*', '-', '+']
    op4 = ['-', '*', '+']
    op5 = ['+', '-', '*']
    op6 = ['*', '+', '-']
    operator = [op1, op2, op3, op4, op5, op6]

    candi = []
    for op in operator:
        e = re.split('([-+*])', expression)
        # print(e)
        ex = Maximize(op, e)
        candi.append(ex)

    # print(candi)
    return max(candi)


expression = "100-200*300-500+20"
sol = solution(expression)
print(sol)