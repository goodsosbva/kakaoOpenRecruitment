# 카카오 공채 2019년 - 후보키
from itertools import chain, combinations

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],\
            ["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]


# 모든 부분집한(열의 쌍)을 구하는 함수
def getAllSubset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


# 부분 집한 중에서 유일성을 만족하는 부분집합(열의 쌍) 구하는 함수
def getAllUniqueSubset(relation):
    subsetList = getAllSubset(list(range(0, len(relation[0]))))
    # print(list(subsetList))
    uniqueList = []
    for subset in subsetList:
        unique = True
        rowSet = set()
        for i in range(len(relation)):
            row = " "
            for j in subset:
                # print(subset)
                row += relation[i][j] + "."
            print(row)
            if row in rowSet:
                unique = False
                break
            rowSet.add(row)
        if unique:
            uniqueList.append(subset)
        print("====", uniqueList)

    return uniqueList

k = getAllUniqueSubset(relation)
print(k)


# 최소성
def sol(relation):
    uniqueList = getAllUniqueSubset(relation)
    uniqueList = sorted(uniqueList, key=lambda x: len(x))

    print("start!!!!!!!!!!!!!!!", uniqueList)
    ansList = []
    for subset in uniqueList:
        # print(subset)
        subset = set(subset)
        # print(subset)
        chk = True
        for j in ansList:
            # 부분 집합인지 확인 ( 최소성 체크 )
            if j.issubset(subset):
                chk = False
        if chk == True:
            ansList.append(subset)

    return len(ansList)


sol = sol(relation)
print(sol)