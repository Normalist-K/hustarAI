# 피보나치 - DP

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")


def fibo_dp(n):
    fibo = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        if i in (1, 2):
            fibo[i] = 1
        else:
            fibo[i] = fibo[i-1] + fibo[i-2]
    
    return fibo[-1]

def fibo_dp2(n):
    
    for i in range(1, n + 1):
        if i in (1, 2):
            fibo_last = 1
            fibo_i = 1
            fibo_ii = 1
        else:
            fibo_last = fibo_i + fibo_ii
            fibo_i = fibo_ii
            fibo_ii = fibo_last

    return fibo_last    

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(fibo_dp2(N))
