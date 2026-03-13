# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 15:51:55 2026

@author: human
"""

#%% 1분코딩
pocket=['card', 'paper','smartphone','key']
if 'card' not in pocket:
    print("걸어가라")
else:
    print("버스를 타고 가라")
#%% 예제
prompt="""
1.ADD
2.DEL
3.LIST
4.QUIT
"""
number=0
while number!=4:
    print(prompt)
    number=int(input())

print("PROGRAM EXIT")
#%%1분코딩
a=0
while a<20:
    a=a+1
    if a%3==0: continue
    print(a)
#%%
scores=[100,32,52,64,88]
num=0
for score in scores:
    num=num+1
    if score >= 60:
        print("%d번 학생은 합격입니다." %num)
    else:
        print("%d번 학생은 탈락입니다." %num)
#%%
#my_list와 슬라이싱을 사용하여 홀수 큰수부터 나오게
my_list=[1,2,3,4,5,6,7,8,9,10]
my_list[::2][::-1]
my_list[-2::-2]
#%%
sum=0
for i in range(101):
    sum+=i
print(sum)
#%% 구구단 생성
for i in range(1,10):
    for j in range(1,10):
        print(i*j ,end=" ")
    print('')
#%% 리스트 컴프리헨션
a=[1,2,3,4,5,6,7,8,9,10]
result=[num*3 for num in a]
result1=[num*3 for num in a if num%2==0]
result2=[num*3 for num in a if num%3==0]
result3=[num*5 for num in a if num%2!=0]
result4=[num for num in a if num>=3 if num%2==0]
print(result)
print(result1)
print(result2)
print(result3)
print(result4)
#%%
"""
제3장 되새김문제 시작
"""
#%% 1번
#elif 문에서는 가장 먼저 조건에 부합하는 쪽을 실행하기에 shirt가 출력된다
#%% 2번
result=0
i=1
while i<=1000:
    if i%3==0:
        result+=i
    i+=1
print(result)
#%% 3번
i=0
while True:
    i+=1
    if i>5: break
    print("*"*i)
#%% 4번
for i in range(101):
    print(i)
#%% 5번
A=[70,60,55,75,95,90,80,80,85,100]
total=0
for score in A:
    total+=score
average=total/(len(A))
print(average)
#%% 6번
numbers=[1,2,3,4,5]
result=[num*2 for num in numbers if num%2!=0]
print(result)

#%% 자투리
a=[1,2,3,4,5]    
result=[num*4 for num in a]
result
    
    
    
