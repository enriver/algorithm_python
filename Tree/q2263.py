# 트리의 순회 - G3

import sys

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Tree:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
            return

        self.current_node=self.root

        while True:
            if self.current_node.data > data:
                if self.current_node.left is None:
                    self.current_node.left=Node(data)
                    break
                else:
                    self.current_node=self.current_node.left
            else:
                if self.current_node.right is None:
                    self.current_node.right=Node(data)
                    break
                else:
                    self.current_node=self.current_node.right

    #전위
    def preorder(self):
        def _pre_order(root):
            if root is None:
                pass
            else:
                print(root.data, end=' ')
                _pre_order(root.left)
                _pre_order(root.right)
        _pre_order(self.root)

    #중위
    def inorder(self):
        def _in_order(root):
            if root is None:
                pass
            else:
                _in_order(root.left)
                print(root.data, end=' ')
                _in_order(root.right)
        _in_order(self.root)

    #후위
    def postorder(self):
        def _post_order(root):
            if root is None:
                pass
            else:
                _post_order(root.left)
                _post_order(root.right)
                print(root.data, end=' ')
        _post_order(self.root)


if __name__=="__main__":
    tree=Tree()

    n=int(sys.stdin.readline())
    
    for i in range(2):
        if i==0:
            inorder=list(map(int,sys.stdin.readline().split()))
        if i==1:
            post=list(map(int,sys.stdin.readline().split()))
    
    for i in reversed(post):
        tree.insert(i)

    tree.preorder()