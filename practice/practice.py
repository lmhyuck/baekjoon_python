# -*- coding: utf-8 -*-
"""
6강 pdf 연습문제
"""
#%% 1번 
number=input()

if int(number)%2==0:
    print("even")
else:
    print("odd")
#%% 3번
final=0
fee=1000
expense=int(input("음식비를 입력하세요: "))
if expense>=30000:
    expense-=3000
elif expense>=20000:
    expense-=2000
else:
    expense=expense
final=expense+fee
print(final)

#%% 4번
score= int(input())
if score >= 90:
    print("수")
elif score >= 80:
    print("우")
elif score >= 70:
    print("미")
elif score >= 60:
    print("양")
else:
    print("가")
    
#%% 5번
dict={"ID1": "PS1", "ID2":"PS2", "ID3": "PS3", "ID4":"PS4"}
id=input("id를 입력하세요.:")
if not id in dict.keys():
    print("ID가 없습니다.")
else:
    ps=input("비밀번호를 입력해주세요:")
    if ps != dict[id]:
        print("비밀번호가 다릅니다.")
    else:
        print("로그인 되셨습니다.")
#%% 6번
dict={"ID1": "PS1", "ID2":"PS2", "ID3": "PS3", "ID4":"PS4"}

cnt=0

id=input("id를 입력하세요.:")

if not id in dict.keys():
    print("ID가 없습니다.")
else:
    while True:
        ps=input("비밀번호를 입력해주세요:")
        if ps != dict[id]:
            cnt=cnt+1
            print("비밀번호가 다릅니다.")
        else:
            print("로그인 되셨습니다.")
            break
        if cnt==5:
            del dict[id]
            print("비밀번호 오류 5회로 ID 삭제 진행합니다.")
            break
        else:
            continue
#%% 7번
number=int(input("팩토리얼 계산에 들어갈 숫자를 입력해주세요:"))
result=1
for i in range(1,number+1):
    result=result*i
print(result)
#%% 8번
for i in range(1,18,2):
    print(f'{"*"*i:^20}')
#%% 9번
str=set(input("문자열을 입력해주세요: "))
del_set={'a','i','e','o','u'}
print(str-del_set)
















