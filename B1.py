from typing import List


def solution(n: int, arr1: List[int], arr2: List[int]) -> List[str]:
    maps = []
    for i in range(n):
        # OR 연산 후 이진수 변환
        print(bin(arr1[i] | arr2[i]))
        maps.append(
            bin(arr1[i] | arr2[i])[2:]
                .zfill(n)
                .replace('1', '#')
                .replace('0', ' ')
        )
    return maps


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
sol = solution(n, arr1, arr2)
print(sol)
