# N 바퀴 레이스
from collections import deque

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


def check_rank(rank):
    queue_round = [deque([]) for _ in range(N)]
    dict_round = dict()

    for car in rank:
        if car not in dict_round.keys():
            dict_round[car] = 1
        else:
            dict_round[car] += 1

        r = dict_round[car]

        if r == 1:
            queue_round[r].append(car)
        elif r == N:
            pre_queue = queue_round[r-1]
            if len(pre_queue) != 0 and car == pre_queue[0]:
                pre_queue.popleft()
            else:
                return False
        else:
            pre_queue = queue_round[r-1]
            current_queue = queue_round[r]
            if len(pre_queue) != 0 and car == pre_queue[0]:
                pre_queue.popleft()
                current_queue.append(car)
            else:
                return False

    return True


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    rank = [n for n in map(int, input().split())]

    if check_rank(rank):
        print("NO")
    else:
        print("YES")
