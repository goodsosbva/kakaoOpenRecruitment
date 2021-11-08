# 3. 불량 사용자
import collections


# 올별 제거
def starDel(banned_id):
    idx = 0
    f_length = len(banned_id) - 1
    for id in banned_id:
        if id == '*' * len(id) and idx != f_length:
            del banned_id[idx]
        idx += 1
    """idx = 0
    for id in banned_id:
        if id == '*' * len(id):
            del banned_id[idx]
        idx += 1"""
    return banned_id


# 같은 밴 아이디 제거
def sameBanID(banned_id):
    for i in range(0, len(banned_id) - 1):
        print(banned_id)
        if len(banned_id) < 3:
            break
        if banned_id[i] == banned_id[i + 1]:
            banned_id.remove(banned_id[i])

    if banned_id[0] == banned_id[1]:
        banned_id.remove(banned_id[i])

    return banned_id


# 솔루션
def solution(user_id, banned_id):
    answer = 0
    # 올별 제거
    new_banned_id = starDel(banned_id)
    print(new_banned_id)
    new_banned_id = sameBanID(new_banned_id)
    print(new_banned_id)
    result1 = collections.defaultdict(int)
    result2 = collections.defaultdict(int)
    ans = []
    for str1 in user_id:
        for str2 in new_banned_id:
            idx = 0
            cnt = 0
            # print(str1, str2)
            for _ in range(len(str1)):
                if len(str1) != len(str2):
                    break
                if str1[idx] == str2[idx] or str2[idx] == '*':
                    cnt += 1
                idx += 1
            if cnt == len(str2):
                # ans.append(str2)
                result1[str1] += 1
                result2[str2] += 1
        print(result1, result2)
        if ans:
            answer += 1
            ans = []

    print(answer)

    return answer


user_id1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user_id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user_id3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id1 = ["fr*d*", "abc1**"]
banned_id2 = ["*rodo", "*rodo", "******"]
banned_id3 = ["fr*d*", "*rodo", "******", "******", "******"]

sol = solution(user_id3, banned_id3)