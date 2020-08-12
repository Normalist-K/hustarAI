import bisect
from queue import Queue

# import sys
# sys.stdin = open("./exercise/hustar03/06.txt", "r")

def BFS(graph, visited, candidates):

    while not candidates.empty():
        current = candidates.get()
        if current not in visited:
            visited.append(current)
        
            for node in graph[current]:
                if node not in visited:
                    candidates.put(node)

    return visited

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]

    for _ in range(M):
        u, v = map(int, input().split())
        bisect.insort_left(graph[u], v)

    visited = []
    candidates = Queue()
    candidates.put(0)

    print(*BFS(graph, visited, candidates))
    
