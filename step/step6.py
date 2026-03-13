# -*- coding: utf-8 -*-
"""
백준단계별 문제 6단계
"""
#%% 6-1단계 25083번
print("         ,r'\"7")
print("r`-_   ,'  ,/")
print(" \. \". L_r'")
print("   `~\/")      
print("      |")      
print("      |")      
#%% 6-2단계 3003번
white=list(map(int,input().split()))
correct=[1,1,2,2,2,8]
result=[]
for i in range(6):
    result.append(correct[i]-white[i])
    print(result[i], end=" ")
print("")
#%% 6-3단계 2444번
num=int(input())
for i in range(1,num+1,1):
    print((num-i)*" "+(i*2-1)*"*")
for i in range(num-1,0,-1):
    print((num-i)*" "+(i*2-1)*"*")

#%% 6-4단계 10988번
word6_4=input()
if word6_4==word6_4[::-1]:
    print(1)
else:
    print(0)
#%% 6-5단계 1157번
word6_5=input().lower()
word_list=list(set(word6_5)) #중복 제외한 문자 리스트
result=[]
for i in word_list:
    cnt=word6_5.count(i)
    result.append(cnt)
if result.count(max(result))>1:
    print("?")
else:
    print(word_list[result.index(max(result))].upper())
#%% 6-6단계 2941번
word6_6=input()
croatia=["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in croatia:   
    word6_6=word6_6.replace(i,"*")          
print(len(word6_6))
#%% 6-7단계 1316번      
n=int(input())
count=0
for _ in range(n):
    word6_7=input()
    check=True
    for i in range(len(word6_7)-1):
        if word6_7[i]!=word6_7[i+1]:
            if word6_7[i] in word6_7[i+1:]:
                check=False
                break
    if check:
        count+=1
print(count)
#%% 6-8단계 25206번 
grade_dict={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
total_score=0
total_credit=0
for _ in range(20):
    subject=input().split()
    if subject[2]!="P":
        total_score+=float(subject[1])*grade_dict[subject[2]]
        total_credit+=float(subject[1])
print(total_score/total_credit)