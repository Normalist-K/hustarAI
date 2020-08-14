# 강변 공원 조성

# 스택 2개 / 시간 복잡도 n

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    houses = [house for house in map(int, input().split())]
    
    stack = []

    for idx in range(len(houses)):
        pass

    print()
