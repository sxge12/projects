list1 = [2, 5, 8, 12]
list2 = [7, 3, 9, 14]
list3 = [1, 4, 10, 6]


def s_m(whichlist):
    summ = 0

    for i in range(4):
        summ += whichlist[i]



def maxx(max_list):
            m_x = 0
            for i in range(1, 4):
                if m_x < max_list[i]:
                    m_x = max_list[i]
            return m_x


sum1 = sum(list1)
max1 = maxx(list1)
sum2 = sum(list2)
max2 = maxx(list2)
sum3 = sum(list3)
max3 = maxx(list3)

print(sum1)
print(max1)

print(sum2)
print(max2)

print(sum3)
print(max3)

