import sys

input=sys.stdin.readline

class Node:
    def __init__(self, data=None):
        self.data=data
        self.left=None
        self.right=None
        

def inorder(node = Node):
    if node:
        inorder(node.left)
        print(node.data, end='')
        inorder(node.right)
        
def preorder(node = Node):
    if node:
        print(node.data, end='')
        preorder(node.left)
        preorder(node.right)
        
def postorder(node = Node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end='')
        
N=int(input())
tree={}

# 모든 노드 생성 및 연결
for i in range(N):
    root_d,left_d,right_d=input().split()
    if i == 0 :
        first=root_d
    # 현재 노드가 없으면 생성 , 있으면 가져오기
    if root_d not in tree:
        tree[root_d]=Node(root_d)
    if left_d != '.':
        tree[left_d]=Node(left_d)
        tree[root_d].left=tree[left_d]
    if right_d != '.':
        tree[right_d]=Node(right_d)
        tree[root_d].right=tree[right_d]
        

preorder(tree[first])
print()
inorder(tree[first])
print()
postorder(tree[first])
