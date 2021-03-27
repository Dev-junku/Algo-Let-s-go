genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def bubble_sort(queue):                                                #우연치 않게도 1번인덱스가 둘다 합으로 들어감
    if len(queue) >= 2:
        for i in range(len(queue)):
            for j in range(len(queue) - 1):
                if queue[j][1] > queue[j + 1][1]:
                    queue[j], queue[j + 1] = queue[j + 1], queue[j]

        return queue
    return queue


def solution(genres, plays):

    queue = []
    dict1 = {}
    ans = []
    genre_sort = []
    result = []
    for idx in range(len(genres)):
        queue += [[genres[idx], plays[idx], idx]]

    bubble_sort(queue)                               #queue 재생순서대로 정렬

    set_queue = list(set(genres))                     #장르 교집합

    for i in range(len(set_queue)):
        sum_genre = 0
        for idx in range(len(queue)):
            if set_queue[i] == queue[idx][0]:
                sum_genre += queue[idx][1]               #같은 장르끼리 함
                genre_sort += [queue[idx]]               #정렬된 queue순서대로 장르별로 묶음
        ans += [[set_queue[i],sum_genre]]
    bubble_sort(ans)                                     #장르별 합 정렬

    for idx in range(len(genre_sort)-1):
        if genre_sort[idx][1] == genre_sort[idx + 1][1]:
            if genre_sort[idx][2] < genre_sort[idx+1][2]:
                genre_sort[idx], genre_sort[idx+1] = genre_sort[idx+1], genre_sort[idx]           #3번 조건 재생횟수같으면 고유번호 낮은 노래 먼저수록될수 있게끔 재생횟수 같으면 낮은번후가 뒤로가게함
    # print(genre_sort)
    for i in range(len(ans)-1,-1,-1):                                       #낮은순서부터 따라서 출력은 거꾸로
        cnt = 0
        for idx in range(len(genre_sort)-1,-1,-1):           #뒤에서부터 확인(2개씩)
            if ans[i][0] == genre_sort[idx][0]:
                result.append(genre_sort[idx][2])
                cnt += 1
                if cnt == 2:
                    break
    return result
solution(genres, plays)