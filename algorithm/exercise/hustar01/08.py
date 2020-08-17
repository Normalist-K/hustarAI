# 마을 회관

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    houses = [num for num in map(int, input().split())]

    min_dist = 0

    for idx in range(len(houses)):
        if idx < (len(houses) // 2):
            min_dist -= houses[idx]
        else:
            min_dist += houses[idx]

    print(min_dist)
