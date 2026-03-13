#%% 7-1단계 2738번
row, col=map(int,input().split())
matrix1=[]
for i in range(row):
    data1=list(map(int,input().split()))
    matrix1.append(data1)
matrix2=[]
for i in range(row):
    data2=list(map(int,input().split()))
    matrix2.append(data2)
for i in range(row):
    for j in range(col):
        print(matrix1[i][j]+matrix2[i][j], end=' ')
    print()
#%% 7-2단계 2566번
