N = int(input())
card_1 = list(map(int, input().split()))
M = int(input())
card_2 = list(map(int, input().split()))

card_dic = {}

for card in card_1:
    try:
        card_dic[card] += 1
    except:
        card_dic[card] = 1

res = []
for card in card_2:
    try:
        res.append(card_dic[card])
    except:
        res.append(0)

print(*res)