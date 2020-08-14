# MST

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

def find(v):
    global root
    if v == root[v]:
        return v
    else:
        root[v] = find(root[v])
        return root[v]

def union(u, v):
    global root, rank
    ru = find(u)
    rv = find(v)
    if rank[ru] > rank[rv]:
        root[rv] = ru
    else:
        root[ru] = rv
        if rank[ru] == rank[rv]:
            rank[ru] += 1

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 간선의 정보를 저장할 리스트
    e = []
    for _ in range(M):
        u, v, c = map(int, input().split())
        # 간선의 비용이 가장 앞에 오도록 저장
        e.append((c, u, v))
    # 간선을 비용의 오름차순으로 정렬
    e.sort()
    # 선택한 간선의 수
    edge_num = 0
    # rank와 root 초기화
    rank = [0 for _ in range(N)]
    root = [i for i in range(N)]
    total_cost = 0
    # 비용이 작은 간선부터 탐색
    for c, u, v in e:
        if find(u) == find(v):
            continue
        else:
            total_cost += c
            union(u, v)

    print(total_cost)


