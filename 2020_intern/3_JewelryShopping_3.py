# 보석 쇼핑_3
# "투 포인터"를 이용해서 풀어보자!


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
    rdx = len(gems)
    candidate = []

    # 오
    while ldx <= rdx:
        candi = gems[ldx: rdx]
        tr = rdx
        # 오른쪽 포인터
        if chk(candi, target):
            candidate.append([ldx, rdx, rdx - ldx])
            rdx -= 1

        # 포인터 이동이 없다는 뜻
        if tr == rdx:
            break

    if not chk(candi, target):
        rdx += 1

    # print("중간 점검:", ldx, rdx, candidate)

    # 왼
    order = 0
    while ldx <= rdx:
        candi = gems[ldx: rdx]
        tl = ldx
        # 왼쪽 포인터
        if chk(candi, target):
            candidate.append([ldx + 1, rdx, rdx - ldx])
            ldx += 1

        # 포인터 이동이 없다는 뜻
        if tl == ldx:
            break

    if not chk(candi, target):
        ldx -= 1

    # print("최종 점검:", ldx, rdx)

    candidate = sorted(candidate, key=lambda x: (x[2], -x[0]))
    # print(candidate)
    answer = candidate[0][:2]

    return answer


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]  # [0, 7]
gems1 = ["AA", "AB", "AC", "AA", "AC"]
sol = solution(gems1)
print(sol)