# n^k 의 mod 구하기

# import sys
# sys.stdin = open("02.txt", "r")

def pow_mod(n, k, m):
    if n == 1 or k == 0:
        return 1
    if n == 0:
        return 0 
    if k == 1:
        return n

    half = pow_mod(n, k//2, m)

    if k % 2 == 0:
        return (half * half) % m
    else:
        return (half * half * n) % m

T = int(input())
for test_case in range(1, T + 1):
    n, k, m = map(int, input().split())
    print(pow_mod(n, k, m))