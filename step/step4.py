# -*- coding: utf-8 -*-
"""
백준 단계별 문제  4단계
"""
#%% 4-1단계 10807번
num=int(input()) #주어진 정수의 개수 N
numbers=list(map(int,input().split()))
v=int(input())
cnt=0
for j in numbers:
    if j==v:
        cnt+=1
print(cnt)
#%% 4-2단계 10871번
N , X =map(int, input().split())
a=list(map(int,input().split()))
result=[]
for i in a:
    if i<X:result.append(i)
for i in result:
    print(i, end=" ")
#%% 4-5단계 10810번
n,m=map(int, input().split())
bucket=[]
for i in range(n):
    bucket.append(0)
for i in range(m):
    a,b,c=map(int, input().split())
    bucket[(a-1):b]=[c]*(b-(a-1))
for i in bucket:
    print(i, end=" ")
#%% 4-6단계 10813번
n,m=map(int, input().split())
bag=[]
for i in range(n):
    bag.append(i+1)
for i in range(m):
    a,b=map(int, input().split())
    bag[a-1],bag[b-1]=bag[b-1], bag[a-1]
for i in bag:
    print(i, end=" ")
#%% 4-7단계 5597번
students={0,}
compare={0,}
for i in range(1,31):
    students.add(i)
for i in range(28):
    num=int(input())
    compare.add(num)
result=[]
for i in (students-compare):
    result.append(i)
result.sort()
for i in result:
    print(i)
#%% 4-9단계 10811번
n,m=map(int, input().split())
bucket=[]
for i in range(n):
    bucket.append(i+1)
for i in range(m):
    j,k=map(int, input().split())
    bucket[j-1:k]=reversed(bucket[j-1:k])
for i in bucket:
    print(i, end=" ")
#%% 4-10단계 1546번
exam=int(input())
scores=input().split()
num=0
for i in scores:
    scores[num]=int(i)
    num+=1
max_score=max(scores)
result=0
for i in scores:
    result+=(i/max_score*100)
print(result/len(scores))


    



























    