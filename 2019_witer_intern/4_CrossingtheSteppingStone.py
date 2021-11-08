# 4. 징검다리 건너기


def solution(stones, k):
    answer = 0
    jump = 0
    idx = 0
    while True:
        if idx >= len(stones):
            answer += 1
            idx = 0
        print(stones)
        for j in range(1, k + 1):
            if j == k and stones[idx + k - 1] == 0:
                return answer

            if idx + j - 1 >= len(stones):
                answer += 1
                idx = 0
                jump = 0
                break
            # print(idx + j - 1)
            if stones[idx + j - 1] > 0:
                stones[idx + j - 1] -= 1
                jump = j
                break

        idx += jump

    return answer


k = 3
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
ans = solution(stones, k)
print(ans)