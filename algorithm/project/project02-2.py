import heapq
# import sys
# sys.stdin = open("project02-2.txt", "r")

class DualPriorityQueue:
    def __init__(self):
        self.hq_max = []
        self.hq_min = []
    
    def insert(self, num):
        is_pop = [False]
        heapq.heappush(self.hq_max, (-num, is_pop))
        heapq.heappush(self.hq_min, (num, is_pop))

    def minpop(self):
        min_elem = heapq.heappop(self.hq_min)
        if min_elem[1][0] == False:
            min_elem[1][0] = True
            return min_elem[0]
        else:
            return self.minpop()

    def maxpop(self):
        max_elem = heapq.heappop(self.hq_max)
        if max_elem[1][0] == False:
            max_elem[1][0] = True
            return - max_elem[0]
        else:
            return self.maxpop()

t = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, t + 1):
    
    dual_pq = DualPriorityQueue()

    for _ in range(int(input())):
        num = int(input())
        if num == -1:
            print(dual_pq.minpop())
        elif num == -2:
            print(dual_pq.maxpop())
        else:
            dual_pq.insert(num)