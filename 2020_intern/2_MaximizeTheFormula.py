# 2. 수식 최대화

def solution(expression):
    answer = 0
    tmp = ""
    n1 = ""
    n2 = ""
    step = 0
    ex = ""
    for i in expression:
        if i != "*" or i != "-" or i != "+":
            tmp += i
        elif i == "*" or i == "-" or i == "+" and step == 0:
            n1 += tmp
            step = 1
            tmp = ""
            ex += i
        else:
            n2 += tmp
            eval(n1 + ex + n2)


    return answer


expression = "100-200*300-500+20"