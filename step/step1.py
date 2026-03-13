# -*- coding: utf-8 -*-
"""
백준 단계별 문제 1단계
"""
#%% 1-7단계 10926번
name=input()
print(f'{name}??!')
#%% 1-8단계 18108번
year=int(input())
if (year>=1000 and year<=3000):print(year-543)
else:print("잘못된 부릭 연도 입력입니다.")
#%% 1-11단계 11382번
a,b,c=map(int, input().split())
print(a+b+c)
