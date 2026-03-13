#1927번 최소 힙 문제
#코테 대비로 앞으로는 input() 보다는 readline을 사용하도록 하자

import heapq
import sys

input=sys.stdin.readline

N=int(input())
heap=[]
result=[]
for i in range(N):
    input_data=int(input())
    if input_data == 0:
        try:
            result.append(heapq.heappop(heap))
        except IndexError:
            result.append(0)
    else:
        heapq.heappush(heap,input_data)
    
    
sys.stdout.write('\n'.join(map(str,result)))

