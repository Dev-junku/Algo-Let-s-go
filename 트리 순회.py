N = int(input())

# 전위
def preorder(string):
    print(string.node, end='')
    if string.left != '.':
        preorder(tree[string.left])
    if string.right != '.':
        preorder(tree[string.right])

# 중위
def inorder(string):
    if string.left != '.':
        inorder(tree[string.left])
    print(string.node, end='')   
    if string.right != '.':
        inorder(tree[string.right])

# 후위
def postorder(string):
    if string.left != '.':
        postorder(tree[string.left])
    if string.right != '.':\
        postorder(tree[string.right])
    print(string.node, end='')


# 클래스 활용, 단지 딕셔너리에 받아두기만 할거임.
class Tree:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right= right


tree_info = [[] for _ in range(N)]
tree = {}
for i in range(N):
    # 1 데이터 받기
    info = list(input().split())

    # 2-1 받은 데이터를 클래스로 묶어서 딕셔너리로 저장
    # 2-2 중요한건 키 값도 class에 전부 포함해서 넣어줌
    # 2-3 왜냐하면, print로 알파벳 출력할 때 필요함.
    tree[info[0]] = Tree(node=info[0], left=info[1], right=info[2])


preorder(tree['A']) # 출력
print() # 띄워주고
inorder(tree['A']) # 출력
print()
postorder(tree['A']) # 출력