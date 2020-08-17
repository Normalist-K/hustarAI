# 강변 공원 조성

import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalistui-MacBookPro.local'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    houses = [house for house in map(int, input().split())]

    # 스택 구성요소: [idx, 수직거리, 수평거리(시작 idx)]
    stack = []
    # 현재까지 가장 큰 공원 넓이
    max_size = 0

    # 0번째 집 스택에 추가
    stack.append([0, houses[0], 0])

    # 1번 집부터 끝까지 for문
    for idx in range(1, len(houses)):
        # 직전 집의 수직거리보다 더 클 때: 스택에 추가
        if houses[idx - 1] < houses[idx]:
            stack.append([idx, houses[idx], idx])
        # 직전 집의 수직거리보다 작거나 같을 때
        else:
            # 스택의 마지막 원소인 집의 수직거리가 현재 인덱스 집 수직거리보다 크면 pop해서 넓이 구한 다음에 더 큰 넓이 update
            while stack != [] and stack[-1][1] > houses[idx]:
                _, h, s = stack.pop()
                w = idx - s
                max_size = max(max_size, w * h)
            # 스택이 비어있으면, 현재 인덱스에 있는 집이 지금까지 집 중 가장 작은 수직거리이므로 0 인덱스부터 지금까지 넓이 소급
            if stack == []:
                stack.append([idx, houses[idx], 0])
            # 스택 마지막 원소의 수직거리가 현재의 수직거리와 같으면, 해당 원소의 인덱스 값 업데이트
            elif stack[-1][1] == houses[idx]:
                stack[-1][0] = idx
            # 스택 마지막 원소의 수직거리가 현재의 수직거리보다 낮으면, 그 다음 인덱스로 수평거리 추가
            elif stack[-1][1] < houses[idx]:
                stack.append([idx, houses[idx], stack[-1][0] + 1])

    while stack != []:
        _, h, s = stack.pop()
        w = len(houses) - s
        max_size = max(max_size, w * h)

    print(max_size)
