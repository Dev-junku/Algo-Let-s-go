def cycle(query, rows, columns):
    global mat, direction, copy_mat

    r1, c1, r2, c2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1

    width = c2 - c1 + 1
    height = r2 - r1 + 1
    c1 -= 1
    d_num = 0
    change_num = []
    d = 1

    while d_num < 2:
        for i in range(width):
            c1 += d
            change_num.append(mat[r1][c1])
            if i != width-1:
                copy_mat[r1][c1+d] = mat[r1][c1]
                
        copy_mat[r1+d][c1] = mat[r1][c1]
        
        width -= 1
        height -= 1
        
        for i in range(height):
            r1 += d
            change_num.append(mat[r1][c1])
            if i != height-1:
                copy_mat[r1+d][c1] = mat[r1][c1]
                

        d = -1
        if d_num == 1:
            copy_mat[r1-1][c1] = mat[r1][c1]
        else:
            copy_mat[r1][c1+d] = mat[r1][c1]
        
        d_num += 1
    
    for j in range(rows):
        for i in range(columns):
            if copy_mat[j][i] != 0:
                mat[j][i] = copy_mat[j][i]
    
    return min(change_num)


def solution(rows, columns, queries):
    global mat, copy_mat
    mat = [[] for _ in range(rows)]
    copy_mat = [[] for _ in range(rows)]
    for i in range(1, rows+1):
        for j in range(1, columns+1):
            mat[i-1].append((i-1)*columns+j)
            copy_mat[i-1].append(0)
    ans = []
    
    for query in queries:
        ans.append(cycle(query, rows, columns))
        
    return ans


if __name__ == '__main__':
    print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
    print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
    print(solution(100, 97, [[1,1,100,97]]))