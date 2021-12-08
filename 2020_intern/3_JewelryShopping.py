# 3. 보석 쇼핑


def chk(gems, candi):
    onlyGems = list(set(gems))
    onlyCandi = list(set(candi))

    # print(onlyGems, onlyCandi)

    cnt = 0
    ok_cnt = len(onlyGems)
    for g in onlyCandi:
        if g in onlyGems:
            cnt += 1
    if cnt == ok_cnt:
        return True
    else:
        return False


def solution(gems):
    answer = []
    candi = []

    # 정방향
    for g in range(len(gems)):
        gem = list(set(gems[0: g + 1]))
        # if gem in gems[g + 1:]:
        sdx = g
        for g1 in gem:
            # print("gem:", gem, g1)
            if g1 in gems[g + 1:]:
                edx = gems[g + 1:].index(g1) + 1
            else:
                edx = len(gems)
            # print(sdx, edx)
            candi = gems[sdx: edx]
            # print("candi1", candi)
            if candi:
                # 끝단 중복 제거
                if candi[0] in candi[1:]:
                    candi.pop(0)
                    sdx -= 1
                elif candi[-1] in candi[:len(candi) - 1]:
                    candi.pop()
                    edx -= 1

            # print("candi2", candi)
            if chk(gems, candi):
                answer.append([sdx + 1, edx, abs(sdx + 1 - edx)])
            candi = []

    answer = sorted(answer,  key = lambda x: x[2])
    # print(answer)
    return answer[0][0:2]


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems1 = ["AA", "AB", "AC", "AA", "AC"]
sol = solution(gems1)
print(sol)


"""
if a == len(gems) - 1 and gems[a] == gem:
    edx = a
    break
"""