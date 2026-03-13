# -*- coding: utf-8 -*-
"""
5장 파이썬 날개 달기
"""
#%% 계산기 클래스
class Calculator:
    def __init__(self, first, second):
        self.first= first
        self.second= second
        self.result=0
        
    def add(self):
        self.result=self.first+ self.second
        return self.result
    
    def sub(self):
        self.result= self.first- self.second
        return self.result
    
    def mul(self):
        self.result= self.first*self.second
        return self.result
    
    def div(self):
        if self.second==0:
            return "0으로 나눌 수 없습니다"
        self.result=self.first/self.second
        return self.result
    
cal=Calculator(10,5)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())

#%%
list(filter(lambda x: x>0, [1,-4,3,6,-2,-11,29]))
#%%
def two_times(x):
    return x*2
print(list(map(two_times, [1,2,3,4,5,6])))
#%%
print(list(map(lambda x: x*2, [1,2,3,4,5,6,7])))
#%%
chr(97)
ord('a')
#%%
pow(4,3)
list(range(5))
list(range(2,10))
list(range(1,20,3))
round(4.2)
round(5.29318,3)
sorted([1,4,7,3,2,5,8,90,32])
sum([1,2,3,4,5,6,7,8,9])
#%%
import time
time.asctime(time.localtime(time.time()))
time.ctime()
for i in range(11):
    print(i)
    time.sleep(1)
#%%
import math
math.gcd(20,60,100)
math.lcm(3,6,8)
#%%
import random
random.random()
random.randint(1,100)
my_list=[1,2,3,4,5,6,7,8,10,20,40,55]
print(random.choice(my_list))
print(random.sample(my_list, 5))
#%%
import itertools
list(itertools.permutations(['1','2','3','4'],2))
for a,b in itertools.permutations(['1','2','3','4'],2):
    print(a+b)
print(list(itertools.combinations(['1','2','3','4','5'], 3)))
#%%
import functools
print(functools.reduce(lambda a,b: a if a>b else b, [1,9,4,2,8,6]))
#%%
from operator import itemgetter

students=[{"name":"java", "age":32,"grade":'A'},
          {"name":"paul", "age":12,"grade":'C'},
          {"name":"ruby", "age":24,"grade":'B'}]

result=sorted(students, key=itemgetter("age"))
print(result)
#%%
for i in range(1,4):
    print(f'{"*"*i:>6}')
#%%
from faker import Faker
fake=Faker('ko-KR')
fake.address()
test_data=[(fake.name(),fake.address()) for i in range(20)]
test_data
#%%
from fractions import Fraction
import sympy

x=sympy.symbols('x')
f=sympy.Eq(x*Fraction('2/5'),1760)
print(sympy.solve(f))
#%%
import sympy

x,y=sympy.symbols('x,y')
f1=sympy.Eq(x+y, 10)
f2=sympy.Eq(x-y,4)
result=sympy.solve([f1,f2])
print(result)
"""
5장 되새김 문제 시작
"""
#%% 1번
class Calculator:
    def __init__(self):
        self.value=0
    
    def add(self, val):
        self.value+=val
    
class UpgradeCalculator(Calculator):
    def minus (self, val):
        self.value-=val
        
cal=UpgradeCalculator()
cal.add(10)
cal.minus(7)
print(cal.value)
#%% 2번
class Calculator:
    def __init__(self):
        self.value=0
    
    def add(self, val):
        self.value+=val
class MaxLimitCalculator(Calculator):
    def add(self, val):
        if self.value>=100:
            return 100
        else:
            self.value+=100

cal=MaxLimitCalculator()
cal.add(50)
cal.add(60)
print(cal.value)
    
    
cal=MaxLimitCalculator()
cal.add(50)
cal.add(60)
#%% 3번
"""
1,2는 ture인데 abs(-3)-3은 음수이니 False이고 all에서 한개라도 false면 결과는 False이다
두번째는 'a'를 아스키코드로 바꿨다가 다시 복구하는거이기에 동일하니 True
"""
#%% 4번
list(filter(lambda x : x>=0 , [1,-2,3,-5,8,-3]))
#%% 5번
int('0xea',16)
#%% 6번
list(map(lambda x : x*3, [1,2,3,4]))
#%% 7번
import functools
max_result=functools.reduce(lambda x,y:x if x>y else y, [-8,2,7,5,-3,5,0,1])
min_result=functools.reduce(lambda x,y:x if x<=y else y, [-8,2,7,5,-3,5,0,1])
print(max_result+min_result)
#%% 8번
round(5.66666666666667, 4)
#%% 9번
# os.chdir
# result= os.system("dir")
# print(result.read())
#%% 10번
"""
import glob
glob.glob("C:\doit\*.py")
"""
#%% 11번
import time
time.strftime("%Y/%m/%d %H:%M:%S")
#%% 12번
import random
lotto=[]
while len(lotto)<6:
    num=random.randint(1,45)
    if num not in lotto:
        lotto.append(num)
print(lotto)
#%% 13번
import datetime
sis=datetime.date(1995,11,20)
young=datetime.date(1998,10,6)
diff=sis-young
diff.days
print("%d일 먼저 태어났습니다." %abs(diff.days))
#%% 14번
from operator import itemgetter
from faker import Faker

fake=Faker("ko-KR")
data=[(fake.name(),fake.pyint(10,50)) for i in range(20)]
result_data=sorted(data, key=itemgetter(1))
result_data
#%% 15번
import itertools
cleaner=['나지혜','성성민','윤지현','김정숙']
result=list(itertools.combinations(cleaner, 2))
result
#%% 16번-1방식
str="abcd"
result=1
for i in range(1,len(str)+1):
    result=result*i
print(result)
#%% 16번-2방식    
import itertools
str="abcd"
result=list(itertools.permutations(str, 4))
result
#%% 17번
import itertools
students=['김승현','김진호','강춘자','이예즌','김현주']
doit=['청소','빨래','설거지']
result=list(itertools.zip_longest(students,doit,fillvalue="휴식"))
result
#%% 18번
import math
gcd=math.gcd(200, 80)
result=(200/gcd)*(80/gcd)
print("타일 한선의 길이는 %d입니다." %gcd)
print("필요한 타일의 개수는 %d입니다." %result)
















