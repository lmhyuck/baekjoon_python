#10828번 스택 기본 기능 구현

import sys
input=sys.stdin.readline

N=int(input())

stack=[]
result=[]

for i in range(N):
    input_data=input().split()
    command=input_data[0]
    if command == "push":
        value=input_data[1]
        stack.append(value)
    elif command == "pop":
        try:
            result.append(stack.pop())
        except IndexError:
            result.append(-1)
    elif command == "size":
        result.append(len(stack))
    elif command == "empty":
        if not stack:
            result.append(1)
        elif stack:
            result.append(0)
    elif command == "top":
        try:
            result.append(stack[-1])
        except IndexError:
            result.append(-1)
            
sys.stdout.write('\n'.join(map(str,result)))