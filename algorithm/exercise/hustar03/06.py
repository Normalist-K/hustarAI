import bisect
from queue import Queue

import sys
this_file_name = sys._getframe().f_code.co_filename
sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

def BFS(graph, visited, candidates):

    while not candidates.empty():
        current = candidates.get()
        if visited[current] == False:
            visited[current] = True
            print(current, end=' ')
        
            for node in graph[current]:
                if visited[node] == False:
                    candidates.put(node)

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        bisect.insort_left(graph[u], v)

    visited = [False] * N
    candidates = Queue()
    candidates.put(0)
    BFS(graph, visited, candidates)

    print()
    
