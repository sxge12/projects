from functools import reduce

z = map(lambda n : n*2, [1,2,3,4])
print(list())

f = filter(lambda s: s%2 == 0, [1,2,3,4,5,6,7,8])
print(list())

r = reduce(lambda t,z : t + z, [1,24,4,5])
print()

leest = [1,2,3,4,5,6]

def lamchain(listt):
    map(lambda n : n*2, listt)
    filter(lambda s: s%2 ==0, listt)
    reduce(lambda x,y : x+y,listt)
    print(listt)

lamchain(leest)