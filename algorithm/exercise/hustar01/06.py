# 탐색

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

    nums = [num for num in map(int, input().split())]
    search_nums = [num for num in map(int, input().split())]

    for num in search_nums:
        if num in nums:
            print("YES", end=' ')
        else:
            print("NO", end=' ')

    print()
