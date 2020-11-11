import sys

class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root=None

    # 전위
    def preorder(self, node):
        print(node, end=' ')
        if node.left != None :
            self.preorder(node.left)
        if node.right != None:
            self.preorder(node.right)

    #중위
    def inorder(self, node):
        if node.left != None:
            self.inorder(node.left)
        print(node, end=' ')
        if node.right != None:
            self.inorder(node.right)

    #후위
    def postorder(self,node):
        if node.left != None :
            self.postorder(node.left)
        if node.right != None :
            self.postorder(node.right)
        print(node, end=' ')

    #트리 생성
    def makeTree(self, node, left_node, right_node):
        if self.root==None:
            self.root=node
        node.left=left_node
        node.right=right_node

if __name__=="__main__":
    node=[]
    node.append(Node(1))
    node.append(Node(2))
    node.append(Node(3))
    node.append(Node(4))
    node.append(Node(5))
    node.append(Node(6))
    node.append(Node(7))

    m_tree=Tree()
    for i in range(int(len(node)/2)):
        m_tree.makeTree(node[i], node[i*2+1],node[i*2+2])

    print('전위 순회 : ',end='') ; m_tree.preorder(m_tree.root)
    print('\n'+'중위 순회 : ',end='');  m_tree.inorder(m_tree.root)
    print('\n'+'후위 순회 : ',end='');  m_tree.postorder(m_tree.root)