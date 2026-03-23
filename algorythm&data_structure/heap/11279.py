#11279번 최대 힙 문제
#최대힙 자료 구조는 따로없음
#heappush에서는 value에 음수를 곱하고
# heapq.heappush(heap, -value)
#heappop에서는 최종값에 음수를 곱하면 최대값을 얻어 낼 수 있다
# -heapq.heappop(heap)

import heapq
import sys

input=sys.stdin.readline

heap=[]
result=[]

N=int(input())
for i in range(N):
    input_data=int(input())
    if input_data == 0:
        try:
            result.append(-heapq.heappop(heap))
        except IndexError:
            result.append(0)
    else:
        heapq.heappush(heap,-input_data)
        
sys.stdout.write('\n'.join(map(str,result)))