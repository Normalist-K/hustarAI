# import sys
from random import randint

# sys.stdin = open("project02-1.txt", "r")

# kth 작은 값 찾기
def selection(nums, kth):
    # pivot, nums_less, nums_greather 생성
    # is_unlucky = True
    # while is_unlucky:
    idx = randint(0, len(nums) - 1)
    pivot = nums[idx]
    nums_less = []
    nums_greather = []

    for num in nums:
        if num < pivot:
            nums_less.append(num)
        elif num > pivot:
            nums_greather.append(num)
    
    # size_nums = len(nums)
    size_less = len(nums_less)

        # if size_nums > 7:
        #     if (size_less >= (size_nums / 4)) and (size_less <= (3 * size_nums / 4)):
        #         is_unlucky = False
        # else:
        #     is_unlucky = False
    
    # kth인지 비교
    if kth == size_less + 1:
        value = pivot
    elif kth <= size_less:
        value = selection(nums_less, kth)
    else:
        value = selection(nums_greather, kth - size_less - 1)
    
    return value




t = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, t + 1):
    nums = [num for num in map(int, input().split())]
    kth = int(input())

    min_kth = selection(nums, kth)
    max_kth = selection(nums, len(nums) - kth + 1)

    print(abs(max_kth - min_kth))