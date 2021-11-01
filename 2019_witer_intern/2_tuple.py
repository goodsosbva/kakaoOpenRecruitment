# 2. 튜플

# 풀이 1.
def solution1(s):
    answer = []
    s = s[1:-1]
    # s = s.split("},")
    s = eval(s)
    s = list(s)
    if len(s) != 1:
        s.sort(key=len)
    print(s)
    for i in range(len(s)):
        # print(i, s[i])
        if len(s) == 1:
            answer.append(s[i])
            break
        for j in range(len(list(s[i]))):
            # print(list(s[i])[j])
            if list(s[i])[j] not in answer:
                answer.append(list(s[i])[j])

    return answer


# 풀이 2. 파싱이용
def solution2(s):
    answer = []
    print(s)
    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key=len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer


s0 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s1 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s2 = "{{20,111},{111}}"
s3 = "{{123}}"
s4 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
ans = solution2(s1)
print(ans)