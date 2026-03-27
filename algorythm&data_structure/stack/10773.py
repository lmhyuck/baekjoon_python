import sys
input=sys.stdin.readline

#정수 K개 주어짐
#K개 만큼 장부에 돈이 들어가고 0이 들어오면 가장 최근 금액 지우기
#스택이용해서 0 들어올때 pop하자
stack=[]
result=0
K=int(input())
for _ in range(K):
    money=int(input())
    if money != 0:
        stack.append(money)
    else:
        stack.pop()
for m in stack:
    result+=m
    
print(result)