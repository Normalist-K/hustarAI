# 인접 행렬

import sys
sys.stdin = open("03.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    mat = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(M):
        u, v, c = map(int, input().split())
        mat[u][v] = c
        
    # for row in mat:
    #     for col in row:
    #         print(col, end=' ')
    #     print()

    for i in range(N):
        print(*mat[i])