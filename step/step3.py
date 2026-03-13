# -*- coding: utf-8 -*-
"""
백준단계별 문제 3단계
"""
#%% 3-4단계 25304번
final_price=int(input()) #구매한 물건들의 총 금액
kindOfItem=int(input()) #구매한 물건들의 종류의 수
compare_price=0
while kindOfItem!=0:
    price, num=map(int,input().split()) #각 물건의 가격과 개수
    compare_price+=price*num
    kindOfItem-=1
if final_price==compare_price:print("Yes")
else:print("No")
#%% 3-5단계 25314번
mul=int(input()) #4의 배수 랜덤 입력
if mul%4==0:
    it=int(mul/4)
    for i in range(1,it+1):
        print("long", end=" ")
    print("int")
else:
    print("4의 배수를 입력해주세요")
#%% 3-6단계 15552번
t=int(input())
for i in range(t):
    a,b=map(int, input().split())
    print(a+b)
#%% 3-11단계 10952번
while True:
    a,b=map(int, input().split())
    if a==0 and b==0:
        break
    print(a+b)
