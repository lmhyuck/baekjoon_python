# -*- coding: utf-8 -*-
"""
백준 단계별 문제 5단계
"""
#%% 5-1단계 27866번
s=input()
num=int(input())
print(s[num-1])
#%% 5-2단계 2743번
s=input()
print(len(s))
#%% 5-3단계 9086번
number=int(input())
for i in range(number):
    string=input()
    print(string[0]+string[-1])
#%% 5-4단계 11654번
s=input()
print(ord(s))
#%% 5-5단계 11720번
n=int(input())
number5_5=input()
result5_5=0
for i in range(len(number5_5)):
    result5_5+=int(number5_5[i])
print(result5_5)
#%% 5-6단계 10809번
string5_6=input()
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l',
          'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alphabet:
    print(string5_6.find(i), end=" ")
#%% 5-7단계 2675번
num5_7=int(input())
for i in range(num5_7):
    repeat=input().split()
    repeat_num=int(repeat[0])
    repeat_string=repeat[1]
    for i in repeat_string:
        print(i*repeat_num, end="")
    print("")
#%% 5-8단계 1152번
string5_8=input()
word=len(string5_8.split())
print(word)
#%% 5-9단계 2908번
a,b=map(str,input().split())
new_a=int(a[::-1])
new_b=int(b[::-1])
print(max(new_a,new_b))
#%% 5-10단계 5622번
string5_10=input()
time=0
for i in string5_10:
    if ord(i)>=65 and ord(i)<68:
        time+=3
    elif ord(i)>=68 and ord(i)<71:
        time+=4
    elif ord(i)>=71 and ord(i)<74:
        time+=5
    elif ord(i)>=74 and ord(i)<77:
        time+=6
    elif ord(i)>=77 and ord(i)<80:
        time+=7
    elif ord(i)>=80 and ord(i)<84:
        time+=8
    elif ord(i)>=84 and ord(i)<87:
        time+=9
    elif ord(i)>=87 and ord(i)<91:
        time+=10
print(time)
#%% 5-11단계 11718번
while True:
    try:
        print(input())
    except EOFError:
        break
    























            
        