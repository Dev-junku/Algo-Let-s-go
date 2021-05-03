def solution():
    # 동물 키 순서 리스트
    animal_order = [0] * N

    # 키 순서대로 리스트에 담아주기
    for animal in animals:
        # N 이상의 순서가 나오면 0리턴
        if animal >= N:
            return 0
        else:
            animal_order[animal] += 1

    result = 1
    # 키 순서 리스트의 요소 갯수대로 곱해주기
    for idx in range(len(animal_order)):
        # 반례 걷어내기
        # 동물 종류가 세개 이상이면 0리턴
        if animal_order[idx] > 2:
            return 0
        # 이전 리스트가 이후 리스트보다 짧을때
        if idx > 0 and animal_order[idx-1] < animal_order[idx]:
            return 0

        # 비어있는 요소가 아니라면
        if animal_order[idx]:
            result *= animal_order[idx]
            last = animal_order[idx]

    # 리스트의 마지막이 1로 끝난다면 경우의 수 곱하기 2를 해준다
    if last == 2:
        return result
    elif last == 1:
        return result * 2


N = int(input())
animals = list(map(int, input().split()))

print(solution())

