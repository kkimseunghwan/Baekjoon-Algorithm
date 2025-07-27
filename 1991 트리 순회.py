
from sys import stdin

class Node:
    def __init__(self, node, left = None, right = None):
        self.node = node
        self.left = left
        self.right = right

    # 전위 순회
    def preorder(self):
        
        print(self.node, end='')

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()
    
    def inorder(self):

        if self.left:
            self.left.inorder()

        print(self.node, end='')

        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()
        
        print(self.node, end='')

        
# 이진트리의 노드 개수 N(1 ≤ N ≤ 26)
node_cnt = int(stdin.readline())

# 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다.
tree = {}

for i in range(node_cnt):
    tree[chr(65+i)] = Node(chr(65+i))

# 노드, 자식 정보 입력받기
for i in range(node_cnt):
    node, left, right = map(str, stdin.readline().split())
    tree[node].left = tree[left] if left != '.' else None
    tree[node].right = tree[right] if right != '.' else None

tree["A"].preorder()
print()
tree["A"].inorder()
print()
tree["A"].postorder()

