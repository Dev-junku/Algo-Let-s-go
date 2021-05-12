def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        my_arr = array[i-1 : j]
        my_arr.sort()
        answer.append(my_arr[k-1])
    return answer


"""
파이썬스러운 풀이법..

"""
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))