import sys
import heapq

input=sys.stdin.readline

N=int(input())

heap=[]
result=[]

# heap은 튜플(a,b) 형식으로 저장하면 첫번째 인덱스 데이터를 기준으로 정렬함
for _ in range(N):
    input_data=int(input())
    if input_data==0: #pop 케이스
        try:
            result.append(heapq.heappop(heap)[1])
        except IndexError:
            result.append(0)
    else:
        heapq.heappush(heap, (abs(input_data), input_data))
        
sys.stdout.write('\n'.join(map(str,result)))