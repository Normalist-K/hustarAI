# 가장 가파른 두 점

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    points.sort()

    max_S = 0

    for idx in range(N - 1):
        x1, y1 = points[idx]
        x2, y2 = points[idx + 1]

        S = abs((y1 - y2) / (x1 - x2))

        if S > max_S:
            max_S = S
            max_pair = f"{x1} {y1} {x2} {y2}"

    print(max_pair)
