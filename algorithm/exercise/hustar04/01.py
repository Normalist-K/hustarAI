# 세금 징수

import sys
import socket
com = socket.gethostname()
if com == 'piai-Precision-7920-Tower':
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

def count_coin(tax):
    total = 0
    coins = (50000, 10000, 5000, 1000, 500, 100)

    for coin in coins:
        if tax >= coin:
            count, tax = divmod(tax, coin)
            total += count

    return total    

T = int(input())
for test_case in range(1, T + 1):
    tax = int(input())

    print(count_coin(tax))
