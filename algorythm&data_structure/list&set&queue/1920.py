import sys

input=sys.stdin.readline

N=int(input())
A=set(map(int, input().split()))
M=int(input())
compare=list(map(int, input().split()))
result=[]
for i in range(M):
    if compare[i] in A:
        result.append('1')
    else:
        result.append('0')
        
sys.stdout.write('\n'.join(result))