#1966번 프린터 큐
import sys
from collections import deque

input=sys.stdin.readline

def solve():
    # 우선순위 개수와 찾고자 하는 데이터 인덱스 정보
    n,m=map(int,input().split())
    # 우선순위 리스트형태로 입력 받기
    priorities=list(map(int,input().split()))
    
    dq=deque()
    # 우선순위와 item이 저장된 인덱스 값까지 묶어서 deque에 저장
    for i,p in enumerate(priorities):
        item=(p,i)
        dq.append(item)
    # 몇번째의 우리가 원하는 데이터가 나오는 지 알려줄 변수
    count=0

    while dq:
        # dq에서 최대값을 구하는데 key옵션에 있는 함수를 기준으로 구함
        # lambda로 dq의 item[0]값을 기준으로 최대 item을 구하고 해당 item[0]인 최대 우선순위를 산출
        max_p=max(dq, key=lambda x:x[0])[0]
        # 최대 우선순위를 기준으로 제일 큰 우선순위가 맨앞에 올때까지 rotate진행
        while dq[0][0] != max_p:
            dq.rotate(-1)
        # dq의 맨앞에 있는 녀석이 최대 우선순위가 됬으면 pop 진행
        target= dq.popleft()
        count+=1
        # 원하는 target을 찾은경우
        if target[1] == m:
            return count
    
    
N=int(input())
result=[]
for _ in range(N):
    result.append(solve())
sys.stdout.write('\n'.join(map(str,result)))