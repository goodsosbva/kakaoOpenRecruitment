# 보석 쇼핑_2


def solution(gems):
    candi = []
    for sdx in range(len(gems)):
        target = list(set(gems))
        for edx in range(sdx, len(gems)):
            gem = gems[edx]
            if gem in target:
                target.remove(gem)
            if len(target) == 0:
                candi.append([sdx + 1, edx + 1, abs(sdx - edx)])
                break
    candi = sorted(candi, key = lambda x: x[2])
    print(candi)
    answer = candi[0][:2]
    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
gems1 = ["AA", "AB", "AC", "AA", "AC"]
sol = solution(gems)
print(sol)

# "투 포인터"를 이용해서 풀어보자!