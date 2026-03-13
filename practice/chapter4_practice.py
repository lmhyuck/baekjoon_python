# -*- coding: utf-8 -*-
"""
4장 파이썬 입출력
"""
#%%
def adds(*args):
    result=0
    for i in args:
        result+=i
    return result

print(adds(1,2,3,4,5))
print(adds(1,2,3,4,5,6,7,8,9,10))
#%%
lam= lambda a,b,c : a+b+c
print(lam(1,2,3))
#%% 
f=open("C:\py_practice/test.txt", "w")
for i in range(1,11):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
#%%
f=open("C:\py_practice/test.txt", "r")
while True:
    line=f.readline().strip()
    if not line: break
    print(line)
f.close()
    
#%%
f=open("C://py_practice/test.txt", "r")
lines=f.readlines()
for line in lines:
    print(line.strip())
f.close()
#%%
f=open("C://py_practice/test.txt", "r")
print(f.read())    
f.close()
#%%
f=open("C://py_practice/test.txt", "a")
for i in range(11,21):
    data="%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
#%%
with open("C://py_practice/test2.txt", "w") as f:
    f.write("with문을 사용한 예제입니다.\n")
#%%
"""
4장 되새김 문제 시작
""" 
#%% 1번
def is_odd(number):
    if number%2!=0:
        return True
    else:
        return False
number=int(input())
print(is_odd(number))
#%% 2번
def avg_numbers(*args):
    result=0
    for i in args:
        result+=i
    return result/(len(args))

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))
#%% 3번
input1=input("첫 번째 숫자를 입력하세요: ")
input2=input("두 번째 숫자를 입력하세요: ")

total=int(input1)+int(input2)
print("두 수의 합은 %s입니다" %total)
#input으로 받은 입력값은 문자열로 들어오기 때문에 연산을 하고 싶으면 int형으로 변환이 필요하다
#%% 5번
f1=open("test.txt", "w")
f1.write("Life is too short")
f1.close()
f2=open("test.txt", "r")
print(f2.read())
#%% 6번
user_input=input("저장할 내용을 입력하세요: ")
f=open("test.txt", "a")
f.write("\n")
f.write(user_input)
f.write("\n")
f.close()
#%% 7번
f=open("test.txt", "r")
body=f.read()
f.close()
body=body.replace("java", "python")
f=open("test.txt", "w")
f.write(body)
f.close()







