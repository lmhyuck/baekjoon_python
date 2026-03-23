#9012번 괄호 찾기 문제

import sys

def solve():
    line=sys.stdin.readline().strip()
    if not line:
        return
    
    N=int(line)
    results = []
    
    for i in range(N):
        input_data = sys.stdin.readline().strip()
        balance = 0
        open_chk=0 #괄호가 열린 상태인지 닫힌 상태인지
        for char in input_data:
            if char == '(' :
                balance+=1
                open_chk+=1 
            elif char ==')':
                if open_chk!=0:  #열린 상태인 경우 
                    balance-=1
                    open_chk-=1
                else:
                    balance=1
                    break
                
        if balance != 0: #VP가 아닌 경우 (괄호의 쌍이 맞지 않거나 시작이 열린 괄호가 아닌 경우)
            results.append("NO")
        else:
            results.append("YES")
    sys.stdout.write("\n".join(results))
    
if __name__ == "__main__":
    solve()


