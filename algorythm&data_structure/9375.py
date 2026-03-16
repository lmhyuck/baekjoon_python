import sys

input = sys.stdin.readline

# 테스트 케이스 개수
t = int(input())

for _ in range(t):
    n = int(input())
    
    # 1. 의상 종류별로 개수를 저장할 딕셔너리 (해시)
    clothes = {}
    
    for _ in range(n):
        _, category = input().split()
        
        # 종류별로 카운트
        if category in clothes:
            clothes[category] += 1
        else:
            clothes[category] = 1
            
    # 2. 경우의 수 계산
    # 각 종류별 (개수 + 1)을 모두 곱함
    ans = 1
    for count in clothes.values():
        ans *= (count + 1)
    
    # 3. 알몸인 상태(모든 종류를 안 입은 경우 1가지)를 뺌
    print(ans - 1)