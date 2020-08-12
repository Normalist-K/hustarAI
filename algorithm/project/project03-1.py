# 피보나치 수열

# import sys
# sys.stdin = open("project03-1.txt", "r")

def fibo(n):
    if n in (1, 2):
        return 1

    return fibo(n-1) + fibo(n-2)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(fibo(N))
