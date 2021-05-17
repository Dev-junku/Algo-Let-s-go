def solution(rows, columns, queries):
    ans = []
    
    mat = [[] for _ in range(rows)]
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            mat[i-1].append((i-1)*columns+j)

    for r1, c1, r2, c2 in queries:
        last = mat[r1-1][c2-1]
        min_v = 10001
    
        # 위쪽
        min_v = min(min(mat[r1-1][c1-1:c2-1]), min_v)
        mat[r1-1][c1:c2] = mat[r1-1][c1-1:c2-1]

        # 왼쪽
        for i in range(r1, r2):
            min_v = min(mat[i][c1-1], min_v)
            mat[i-1][c1-1] = mat[i][c1-1]
        
        # 아래쪽
        min_v = min(min(mat[r2-1][c1:c2]), min_v)
        mat[r2-1][c1-1:c2-1] = mat[r2-1][c1:c2]

        # 오른쪽
        for i in range(r2-2, r1-2, -1):
            min_v = min(mat[i][c2-1], min_v)
            mat[i+1][c2-1] = mat[i][c2-1]
        
        mat[r1][c2-1] = last
        min_v = min(min_v, last)

        ans.append(min_v)
    
    return ans

if __name__ == '__main__':
    print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
    print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
    print(solution(100, 97, [[1,1,100,97]]))