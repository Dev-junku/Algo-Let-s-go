parent = []

def who_parent(x):
    if parent[x] != x:
        parent[x] = who_parent(parent[x])
    return parent[x]


def union(x1, x2):
    p1 = who_parent(x1)
    p2 = who_parent(x2)
    
    if p1 > p2:
        parent[p1] = p2
    else:
        parent[p2] = p1


def is_equal(x1, x2):
    return who_parent(x1) == who_parent(x2)


def solution(n, costs):
    global parent
    
    costs.sort(key=lambda x: -x[2])
    parent = [i for i in range(n)]
    res = 0
    
    while costs:
         
        s, e, c = costs.pop()
        
        if not is_equal(s, e):
            union(s, e)
            res += c
    
    return res