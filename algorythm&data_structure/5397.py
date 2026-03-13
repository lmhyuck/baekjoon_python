import sys

input=sys.stdin.readline

def solve():
    N=int(input())
    result=[]
    for _ in range(N):
        input_data = input().strip()
        
        left_stack=[]
        right_stack=[]
        
        for i in input_data:
            if i == "<":
                if left_stack:
                    right_stack.append(left_stack.pop())
            elif i ==">":
                if right_stack:
                    left_stack.append(right_stack.pop())
            elif i =="-":
                if left_stack:
                    left_stack.pop()
            else:
                left_stack.append(i)
            
        result="".join(left_stack)+"".join(reversed(right_stack))
        sys.stdout.write(result+'\n')
    
solve()