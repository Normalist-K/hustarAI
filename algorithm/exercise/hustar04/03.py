# 강변 공원 조성

# 스택 2개 / 시간 복잡도 n

import sys
import socket
com = socket.gethostname()
if com == 'piai-Precision-7920-Tower':
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    houses = [house for house in map(int, input().split())]
    park = len(houses) * min(houses)

    for idx, house in enumerate(houses):
        row = 1
        if idx != 0:
            for left, pre_house in enumerate(houses[idx-1::-1]):
                if pre_house < house:
                    row += left
                    break
            else:
                row += left + 1
        if idx != len(houses) - 1:
            for right, post_house in enumerate(houses[idx+1:]):
                if post_house < house:
                    row += right
                    break
            else:
                row += right + 1
            if park < row * house:
                park = row * house

    print(park)

        

