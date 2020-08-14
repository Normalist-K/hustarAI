# 최장 공통 부분 문자열

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")



T = int(input())
for test_case in range(1, T + 1):
    a = '0' + input() # NULL(dummy) 문자 추가
    b = '0' + input() # NULL(dummy) 문자 추가
    n = len(a)
    m = len(b)
    # dummy 행과 열을 하나씩 추가
    count_mat = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(1, n):
        for j in range(1, m):
            if i == 1 and a[1] == b[j]:
                count_mat[1][j] = 1 
            elif j == 1 and a[i] == b[1]:
                count_mat[i][1] = 1
            elif a[i] == b[j]:
                count_mat[i][j] = max(count_mat[i-1][j-1] + 1, count_mat[i][j-1], count_mat[i-1][j])
            else:
                count_mat[i][j] = max(count_mat[i-1][j], count_mat[i][j-1])
    print(count_mat[-1][-1])
