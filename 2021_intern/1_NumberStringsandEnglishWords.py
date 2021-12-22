# 1. 숫자 문자열과 영단어
numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3,
           'four': 4, 'five': 5, 'six': 6, 'seven': 7,
           'eight': 8, 'nine': 9}


def solution(s):
    answer = []
    st_idx = 0
    for i in range(len(s)):
        num = s[st_idx:i + 1]
        # print(num)
        if num in numbers:
            answer.append(numbers[num])
            st_idx = i + 1
            continue

        if s[i].isdigit():
            answer.append(int(s[i]))
            st_idx = i + 1
            continue

    num = s[st_idx: len(s)]
    if num in numbers:
        answer.append(numbers[num])

    ans = ""
    for s in answer:
        s = str(s)
        ans += s
    # print(ans)
    return int(ans)


s = "123"
s3 = "2three45sixseven"
s2 = "23four5six7"
s1 = "one4seveneight"
sol = solution(s)
print(sol)