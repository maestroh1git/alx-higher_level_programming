#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    sum1 = 0

    if my_list:
        for i in my_list:
            sum = sum + (i[0] * i[1])
            sum1 = sum1 + i[1]
        return sum/sum1
    else:
        return 0
