from itertools import product
from itertools import permutations


def is_match(user, banned):
    if len(banned) != len(user):
        return False

    for i in range(len(banned)):
        if not (banned[i] == '*' or banned[i] == user[i]):
            return False

    return True


def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False  # 현재 튜플 불일치

    return True


def solution(user_id, banned_id):
    # 가능한 모든 경우의 수를 찾은 다음
    user_permutation = list(permutations(user_id, len(banned_id)))
    print(user_permutation)
    banned_Set = []

    # 조건에 맞지 않는 경우의 수 제거 작업
    for users in user_permutation:
        # 하나의 튜플과 비교 시작
        if not check(users, banned_id):
            continue  # 다음 튜플 가져오기

        else:
            users = set(users)
            if users not in banned_Set:
                banned_Set.append(users)

    print(banned_Set)
    return len(banned_Set)



user_id1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user_id2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user_id3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id1 = ["fr*d*", "abc1**"]
banned_id2 = ["*rodo", "*rodo", "******"]
banned_id3 = ["fr*d*", "*rodo", "******", "******", "******"]


ans = solution(user_id1, banned_id1)
print(ans)