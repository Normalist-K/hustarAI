
import sys
import socket
com = socket.gethostname()
if com in ('piai-Precision-7920-Tower', 'Normalist'):
    this_file_name = sys._getframe().f_code.co_filename
    sys.stdin = open(f"{this_file_name[:-3]}.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    
    eventlist = []
    for _ in range(N):
        start, end = map(int, input().split())
        eventlist.append((start, end))

    eventlist.sort(key = lambda event: event[1])
    
    visit_count = 1
    visit_time = eventlist[0][1]
    for start, end in eventlist[1:]:
        if start <= visit_time:
            continue
        visit_time = end
        visit_count += 1

    print(visit_count)

    