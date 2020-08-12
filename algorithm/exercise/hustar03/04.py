# 인접 리스트

# import sys
# sys.stdin = open("04.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(N):
        graph[i].sort()
        print(* graph[i])