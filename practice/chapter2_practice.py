# -*- coding: utf-8 -*-
"""
파이썬 교재 2장 되새김 문제
"""

#%% 1번
a=80
b=75
c=55
avg=(a+b+c)/3
print(avg)
#%% 2번
num=13
if (num%2)==0:
    print("짝수입니다")
else:
    print("홀수입니다")
#%% 3번
personal_id="881120-1068234"
birth= personal_id[:6]
num=personal_id[7:]
print(birth)
print(num)
#%% 4번
pin="881120-1068234"
print(pin[7])
#%% 5번
a="a:b:c:d"
b=a.replace(":", "#")
print(b)
#%% 6번
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)
#%% 7번
a=['Life', 'is', 'too', 'short']
result=" ".join(a)
print(result)
#%% 8번
a=(1,2,3)
a+=(4,)
print(a)
#%% 9번
#Dictionary의 key값은 immutable해야 하기 때문에 3번째 a[[1]]에서 key값으로
#mmutable한 list가 들어갔기 때문에 에러가 발생한다
#%% 10번
a={'A':90, 'B':80, 'C':70}
result=a.pop('B')
print(a)
print(result)
#%% 11번
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)
#%% 12번
a=b=[1,2,3]
a[1]=4
print(b)
#a와 b는 동일 객체를 가르키고 있기 때문에 a리스트의 값을 변경해도 b는 
#동일한 변경된 리스트를 가르키기 때문에 [1,4,3]으로 출력되는 것이다.
#%% 자투리연습
name="이민혁"
age=27
"{0:10.5f}".format(3.14159234)
"{0:;^10}".format("NO")
"{{ and }}".format()
f'안녕하세요 {name}입니다. 나이는 올해 {age}입니다.'
f'{"NO":^10}'
for i in range(1,11):
    print(f'{"*"*i:<10}')
a="?".join("abcde")
"abcd".upper()
"KKDMDKW".lower()







