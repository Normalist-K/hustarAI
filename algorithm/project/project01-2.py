import sys

sys.stdin = open("project01-2.txt", "r")

def check_bracket():

    brackets = input()

    if len(brackets) % 2 == 0:
        stack = []
        for bracket in brackets:
            if bracket in ("(", "{", "["):
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                else:
                    compare = stack.pop()
                    if (compare == "(" and bracket == ")") or (compare == "{" and bracket == "}") or (compare == "[" and bracket == "]"):
                        continue
                    else:
                        return False
        if len(stack) == 0:
            return True
        else: 
            return False
    else:
        return False


t = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, t + 1):
        
    if check_bracket():
        print("YES")
    else:
        print("NO")



