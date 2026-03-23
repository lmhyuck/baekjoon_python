#1874번 : 스택 수열

import sys

# 표준 입력 설정
input = sys.stdin.readline

def solve():
    try:
        n = int(input())
    except ValueError:
        return

    stack = []
    result = []
    current_num = 1  # 다음에 스택에 넣을 숫자 (오름차순 가이드)
    possible = True

    for _ in range(n):
        try:
            target = int(input()) # 문자열을 정수로 변환 (필수)
        except ValueError:
            continue

        # 1. 목표 숫자가 아직 스택에 안 들어왔다면, 들어올 때까지 push
        while current_num <= target:
            stack.append(current_num)
            result.append('+')
            current_num += 1
        
        # 2. 스택의 맨 위(top)가 목표 숫자와 같다면 꺼내기(pop)
        if stack and stack[-1] == target:
            stack.pop()
            result.append('-')
        # 3. top이 목표보다 크다면? (이미 아래 깔린 상태라 꺼낼 수 없음)
        else:
            possible = False

    # 모든 수열을 성공적으로 만들었을 때만 결과 출력
    if possible:
        sys.stdout.write('\n'.join(result))
    else:
        print("NO")

if __name__ == "__main__":
    solve()