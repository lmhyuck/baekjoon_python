import sys

input=sys.stdin.readline

n, m = map(int, input().split())

data_set=set()
for _ in range(n):
    input_data=input().strip()
    data_set.add(input_data)
count=0
for _ in range(m):
    input_data=input().strip()
    if input_data in data_set:
        count+=1
print(count)