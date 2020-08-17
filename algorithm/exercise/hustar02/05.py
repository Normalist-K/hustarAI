# 하노이의 탑

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


def hanoi(N, start, mid, end):
    if N == 1:
        print(f"{start} -> {end}")
    else:
        hanoi(N-1, start, end, mid)
        hanoi(1, start, mid, end)
        hanoi(N-1, mid, start, end)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    hanoi(N, 'A', 'B', 'C')
