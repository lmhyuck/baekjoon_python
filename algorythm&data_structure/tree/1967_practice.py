import sys

input=sys.stdin.readline

N=int(input())

graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    u,v,w=map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))
    

def dfs(node, current_dist, visited, distance):
    if not node:
        return []
    visited[node]=True
    distance[node]=current_dist
    
    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, current_dist+weight, visited, distance)
            
dist1=[-1]*(N+1)
visit1= [False]*(N+1)
dfs(1,0,visit1,dist1)

farther_node= dist1.index(max(dist1))

dist2=[-1]*(N+1)
visit2= [False]*(N+1)
dfs(farther_node,0,visit2,dist2)

print(max(dist2))
