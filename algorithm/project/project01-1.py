t = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, t + 1):
    nums = [num for num in map(int, input().split())]
    targets = [num for num in map(int, input().split())]
    counts = []

    for target in targets:
        counts.append(nums.count(target))

    print(' '.join(map(str, counts)))
    
