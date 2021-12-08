# 보석 쇼핑_5 (l, r 같은 위치에서 개념은 이전이랑 같음 + 딕셔너리 이용 안해보기) -> 시간초과
dic = {}


def chk(g, target):
    cnt = 0
    new_g = list(set(g))
    ok_cnt = len(target)
    for i in new_g:
        if i in target:
            cnt += 1
    if cnt == ok_cnt:
        return True
    return False


def solution(gems):
    target = list(set(gems))
    ldx = 0
    rdx = 0
    candidate = []

    while rdx <= len(gems):
        candi = gems[ldx: rdx]
        # print(gems[ldx: rdx])
        while chk(candi, target):
            candidate.append([ldx, rdx, rdx - ldx, candi])
            ldx += 1
            candi = gems[ldx: rdx]

        rdx += 1

    candidate = sorted(candidate, key=lambda x: (x[2], x[0]))
    # print(candidate)
    ans = [candidate[0][0] + 1, candidate[0][1]]
    return ans


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]  # [0, 7]
gems1 = ["AA", "AB", "AC", "AA", "AC"]
gems2 = ["XYZ", "XYZ", "XYZ"]
gems3 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
sol = solution(gems3)
print(sol)