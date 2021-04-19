def divide(arr, col, row, length):
    start = arr[col][row]
    OK = True
    # 만약에 length가 1이될때까지 쪼갰으면 리턴한다.
    if length == 1:
        answer[start] += 1
        return

    # 만약에 모두 같은 숫자면 하나를 올린다.
    for i in range(col, col+length):
        for j in range(row, row+length):
            if arr[i][j] != start:
                OK = False
                break
    if OK:
        answer[start] += 1
    # 아니라면 다음으로 또 쪼갠다.
    else:
        length = length//2
        divide(arr, col, row, length)
        divide(arr, col+length, row, length)
        divide(arr, col, row+length, length)
        divide(arr, col+length, row+length, length)

answer = [0, 0]
def solution(arr):
    divide(arr, 0, 0, len(arr))
    print(answer)
    return answer

solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1],
     [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]])

