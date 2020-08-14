# 이진 탐색 2

import bisect

# import sys
# sys.stdin = open("project03-2.txt", "r")


def find(nums, search):
    i = bisect.bisect(nums, search)
    if i == 0:
        return nums[0]
    elif i == len(nums):
        return nums[i-1]
    else:
        sub1 = search - nums[i-1]
        sub2 = nums[i] - search
        # return nums[i-1] if sub1 <= sub2 else nums[i]
        if sub1 <= sub2:
            return nums[i-1]
        elif sub1 > sub2:
            return nums[i]

T = int(input())
for test_case in range(1, T + 1):
    nums = [i for i in map(int, input().split())]
    searchs = [i for i in map(int, input().split())]
    answer = []

    for search in searchs:
        answer.append(find(nums, search))

    print(*answer)
