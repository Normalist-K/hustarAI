# 돌다리

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # count = [0 for _ in range(N + 1)] # idx 0은 dummy
        
    # for i in range(1, N + 1):
    #     if i in (1, 2):
    #         count[i] = i
    #     elif i == 3:
    #         count[i] = count[i-1] + count[i-2] + 1
    #     else:
    #         count[i] = count[i-1] + count[i-2] + count[i-3]

    
    for i in range(1, N + 1):
        if i == 1:
            count_3 = 1
            count = count_3
        elif i == 2:
            count_2 = 2
            count = count_2
        elif i == 3:
            count_1 = 4
            count = count_1
        else:
            count = (count_1 + count_2 + count_3) % 1904101441
            count_3 = count_2 % 1904101441
            count_2 = count_1 % 1904101441
            count_1 = count

    print(count)