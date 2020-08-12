# 이진탐색

# import sys
# sys.stdin = open("01.txt", "r")

T = int(input())
for _ in range(T):
    data = list(map(int, input().split()))
    query = list(map(int, input().split()))
    answer = []
    
    for q in query:
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (left + right) // 2
            if data[mid] == q:
                break
            elif data[mid] > q:
                right = mid - 1
            elif data[mid] < q:
                left = mid + 1
                
        if left > right:
            answer.append(-1)
        else:
            answer.append(mid)
            
    print(*answer)