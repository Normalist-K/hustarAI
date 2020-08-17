# 두 바퀴 레이스
from collections import deque

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    rank = [n for n in map(int, input().split())]

    queue = deque([])
    queue.append(rank[0])
    for car in rank[1:]:
        if len(queue) != 0 and car == queue[0]:
            queue.popleft()
        else:
            queue.append(car)

    if len(queue) == 0:
        print("NO")
    else:
        print("YES")
