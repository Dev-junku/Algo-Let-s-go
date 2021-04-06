from sys import stdin


def preorder(node):
    if node:
        print(tree[node][0], end='')
        preorder(tree[node][1])
        preorder(tree[node][2])


def inorder(node):
    if node:
        inorder(tree[node][1])
        print(tree[node][0], end='')
        inorder(tree[node][2])


def postorder(node):
    if node:
        postorder(tree[node][1])
        postorder(tree[node][2])
        print(tree[node][0], end='')


N = int(stdin.readline())
tree = [[0 for _ in range(3)] for _ in range(N+1)]

# index: A를 1, Z를 26으로 저장
a_ord = ord('A')
for _ in range(N):
    parent, child1, child2 = map(lambda x: ord(x) - a_ord + 1, stdin.readline().split())
    tree[parent][0] = chr(parent + a_ord - 1)
    if child1 > 1:
        tree[parent][1] = child1
    if child2 > 1:
        tree[parent][2] = child2

preorder(1)
print()
inorder(1)
print()
postorder(1)
