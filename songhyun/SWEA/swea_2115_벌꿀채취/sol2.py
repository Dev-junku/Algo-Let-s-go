from itertools import combinations
mylist= [1,2,3]
result = combinations(mylist,r=3) # r 생략 불가

print(list(result))
# for i in result:
#     print(sum(i))