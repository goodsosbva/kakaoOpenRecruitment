# 카카오 공채 2019년 - 후보키
from functools import cmp_to_key


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],\
            ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

"""res = []
for i in range(len(relation)):
    tmp = ""
    for j in range(4):
        tmp += relation[i][j]
    res.append(tmp)
print(tmp)
print(res)"""
def compare(a, b):
    x = bin(a).count('1')
    y = bin(b).count('1')
    return x - y


# 모든 튜플이 확인되는지 (두 개씩 쌍을 지어서)
def check(relation, rows, cols, subset):
    # 조합
    # print(subset)
    for a in range(rows - 1):
        for b in range(a + 1, rows):
            isSame = True
            for k in range(cols):
                if (subset & 1 << k) == 0:
                    continue
                if relation[a][k] != relation[b][k]:
                    isSame = False
                    break
            if isSame:
                return False

    return True

rowSize = len(relation)
colSize = len(relation[0])
candi = []

for i in range(1, 1 << colSize):
    # 유일성 체크
    if check(relation, rowSize, colSize, i):
        candi.append(i)
print(candi)
# cmp_to_key: 내가 정렬 방식을 정하는 것
candi = sorted(candi, key=cmp_to_key(compare))
print(candi)
ans = 0
# 최소성 체크
while len(candi) != 0:
    n = candi.pop(0)
    ans += 1
    # n 과 겹쳐지는 비트가 있는건 다시 제외해서 cadi를 만들어 주는 것
    candi = [x for x in candi if (n & x) != n]


print(ans)