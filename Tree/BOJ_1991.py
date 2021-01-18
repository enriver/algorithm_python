# 트리 순회 - S1

import sys

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def preorder(root):  # 전위 순회
    print(root.data, end='')
    if root.left != '.':
        preorder(tree[root.left])
    if root.right != '.':
        preorder(tree[root.right])


def inorder(root):  # 중위 순회
    if root.left != '.':
        inorder(tree[root.left])
    print(root.data, end='')
    if root.right != '.':
        inorder(tree[root.right])


def postorder(root):  # 후위 순회
    if root.left != '.':
        postorder(tree[root.left])
    if root.right != '.':
        postorder(tree[root.right])
    print(root.data, end='')


if __name__ == "__main__":

    N = int(sys.stdin.readline())
    tree = {}

    for _ in range(N):
        data, left, right = map(str, sys.stdin.readline().split())
        tree[data] = Node(data, left, right)

    preorder(tree['A'])
    print()
    inorder(tree['A'])
    print()
    postorder(tree['A'])