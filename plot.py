import numpy as np
import matplotlib.pyplot as plt
import main

d_length = main.d_length
d_top_bit = main.d_top_bit
d_weight = main.d_weight

def plotting(mod_list, mult_list, title):
    #print('mod_list: {0}\nmult_list: {1}'.format(mod_list, mult_list))
    mod_list, mod_count_list = frequency(mod_list)
    print(mod_count_list)
    count = np.array(mod_count_list)
    freq = np.array(mod_list)
    plt.plot(freq, count, label='mod', marker='o')

    mult_list, mult_count_list = frequency(mult_list)
    print(mult_count_list)
    count = np.array(mult_count_list)
    freq = np.array(mult_list)
    plt.plot(freq, count, label='mult', marker='x')

    #plt.xlim(0, 10)
    plt.title('d_length={0}, d_top_bit={1}, d_weight={2}, {3}'.format(d_length, d_top_bit, d_weight, title))
    plt.xlabel('count')
    plt.ylabel('frequency')
    plt.legend(loc = 'upper left')
    plt.show()

def frequency(list):
    max = -1
    for item in list:
        if max <= item:
            max = item

    new_list = [0] * (max+3)
    count_list = []
    k = 0
    for item in new_list:
        count_list.append(k)
        k += 1

    for item in list:
        new_list[item] += 1

    zero_count = 0
    for item in new_list:
        if item == 0:
            zero_count += 1
        else:
            break

    if zero_count >= 2:
        zero_count -= 2
    else:
        zero_count = 0


    del count_list[:zero_count]
    del new_list[:zero_count]



    return count_list, new_list
