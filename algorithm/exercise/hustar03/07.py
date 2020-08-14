# 최대 합 부분 연속 수열

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    nums = [num for num in map(int, input().split())]

    add = max(0, nums[0])
    max_num = nums[0]

    for num in nums[1:]:
        add += num
        max_num = max(max_num, add)
        add = 0 if add <= 0 else add

    print(max_num)
