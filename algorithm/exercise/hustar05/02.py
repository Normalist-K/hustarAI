# 더블로 가

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


def dbro(l, n):
    DP = [0] * len(l)
    for i in range(1, n + 1):
        if i == 1:
            DP[1] = l[1]

        elif i == 2:
            DP[2] = max(DP[1] + l[2], l[2])
        
        elif i % 2 == 0:
            DP[i] = max(DP[i-1] + l[i], DP[i-2] + l[i], DP[i//2] + l[i])

        elif i % 2 == 1:
            DP[i] = max(DP[i-1] + l[i], DP[i-2] + l[i])

    return DP[n]



T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    lis = list(map(int, input().split()))
    lis = [0] + lis
    print(dbro(lis, n))