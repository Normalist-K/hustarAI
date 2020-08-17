# 최댓값 - 최솟값

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

    for idx, num in enumerate(map(int, input().split())):
        if idx == 0:
            max_num = num
            min_num = num
        max_num = max(max_num, num)
        min_num = min(min_num, num)

    print(max_num - min_num)
