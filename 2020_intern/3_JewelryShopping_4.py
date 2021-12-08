# 보석 쇼핑_투포인터 시도 2 + 딕셔너리 사용
dic = {}


def solution(gems):
    answer = [1, 1]
    ans = len(gems) + 1
    gemLen = len(set(gems))
    ldx = 0
    rdx = 0
    while rdx < len(gems):
        if gems[rdx] in dic:
            dic[gems[rdx]] += 1
        else:
            dic[gems[rdx]] = 1

        # 더 좋은 답인지 체크
        if gemLen == len(dic):
            while dic[gems[ldx]] > 1:
                dic[gems[ldx]] -= 1
                ldx += 1
            if ans > (rdx - ldx):
                answer = [ldx + 1, rdx + 1]
                ans = rdx - ldx
        rdx += 1

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]  # [0, 7]
gems1 = ["AA", "AB", "AC", "AA", "AC"]
sol = solution(gems1)
print(sol)