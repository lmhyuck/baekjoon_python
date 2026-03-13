# -*- coding: utf-8 -*-
"""
백준 단계별 문제 2단계
"""
#%% 2-6단계 2525번
A,B=map(int,input().split())
result_A=0
result_B=0
A_plus=0
C=int(input())
if (B+C)>=60:
    result_B=(B+C)%60
    A_plus=(B+C)//60
else:
    result_B=B+C
if (A+A_plus)>=24:
    result_A=(A+A_plus)%24
else:
    result_A=A+A_plus
print(f'{result_A} {result_B}')
    
#%% 2-7단계 2480번
a,b,c=map(int,input().split())
reward=0
if a==b==c:
    reward=10000+a*1000
elif a==b:reward=1000+a*100
elif a==c:reward=1000+a*100
elif b==c:reward=1000+b*100
else:
    reward=max(a,b,c)*100
print(reward)