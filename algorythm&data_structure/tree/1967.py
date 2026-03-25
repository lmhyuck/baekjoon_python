# 루트를 기준으로 가장 멀리 있는 노드 u 찾기
# 노드 u를 기준으로 다시 가장 멀리 있는 노드 v 찾기
# 노드 u,v 사이의 거리가 트리의 지름

# BFS -> 파이썬에서는 list.pop대신 deque.popleft 사용해서 성능 최적화

import sys

# 1. 실무 표준: 재귀 깊이 제한 설정 (트리 높이가 클 경우 필수)
# 기본값은 1000이며, 이를 초과하면 RecursionError가 발생합니다.
sys.setrecursionlimit(10**6)

def solve():
    # 2. 입력 최적화: 대량의 데이터를 빠르게 읽기 위해 사용
    input = sys.stdin.readline

    n = int(input())

    # 3. 인접 리스트 초기화 (가중치 포함)
    # 지름을 구하기 위해 '양방향'으로 저장합니다.
    graph = [[] for _ in range(n + 1)]
    
    for _ in range(n - 1):
        u,v,w=map(int, (input().split()))
        # 양방향 연결: 어느 노드에서 시작해도 전체를 탐색할 수 있게 함
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dfs(node, current_dist, visited, distances):
        """
        깊이 우선 탐색을 통해 시작점으로부터 모든 노드까지의 거리를 계산
        """
        visited[node] = True
        distances[node] = current_dist
        
        # graph.get() 대신 인덱스로 접근
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, current_dist + weight, visited, distances)

    try:
        # [STEP 1] 임의의 노드(1번)에서 가장 멀리 있는 노드(A) 찾기
        dist1 = [-1] * (n + 1) # 미방문 노드를 -1로 표시
        visit1 = [False] * (n + 1) # 초기 False 세팅 이후 방문 시마다 True로 변환
        dfs(1, 0, visit1, dist1)
        
        # 가장 먼 노드의 번호 찾기
        farthest_node = dist1.index(max(dist1))

        # [STEP 2] 노드(A)에서 다시 가장 멀리 있는 노드(B) 찾기
        dist2 = [-1] * (n + 1)
        visit2 = [False] * (n + 1)
        dfs(farthest_node, 0, visit2, dist2)

        # [결과] A와 B 사이의 거리가 트리의 지름
        print(max(dist2))

    except Exception as e:
        print(f"[Runtime Error] 탐색 중 오류 발생: {e}")

if __name__ == "__main__":
    solve()
    
