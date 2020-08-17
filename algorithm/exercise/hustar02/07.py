# 수의 곱

import heapq

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    hq = []
    heapq.heappush(hq, 1)
    for num in map(int, input().split()):
        heapq.heappush(hq, num)
