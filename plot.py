import numpy as np
import matplotlib.pyplot as plt
import main

d_length = main.d_length
d_top_bit = main.d_top_bit
d_weight = main.d_weight
loop_times = main.Loop_times

def plotting(mod_list, mult_list, title):

    mod_count_list, mod_freq_list = frequency(mod_list)
    mult_count_list, mult_freq_list = frequency(mult_list)

    mod_list_length = len(mod_count_list)
    mult_list_length = len(mult_count_list)

    mod_count_list = np.pad(mod_count_list, [0, (mult_list_length - mod_list_length)], 'constant')
    mod_freq_list =  np.pad(mod_freq_list, [0, (mult_list_length - mod_list_length)], 'constant')

    mod_argmax = np.argmax(mod_freq_list)
    mult_argmax = np.argmax(mult_freq_list)

    print('最大値のインデックスは, mod: {0}, mult: {1}'.format(mod_argmax, mult_argmax))

    mod_freq = np.array(mod_freq_list)
    mod_count = np.array(mod_count_list)
    plt.plot(mod_count, mod_freq, label='mod', marker='o')

    mult_freq = np.array(mult_freq_list)
    mult_count = np.array(mult_count_list)
    plt.plot(mult_count, mult_freq, label='mult', marker='x')

    """
    sum_freq = mod_freq + mult_freq
    sum_argmax = np.argmax(sum_freq)
    print('最大値のインデックスは, sum: {0}'.format(sum_argmax))
    plt.plot(mult_count, sum_freq, label='sum', marker='v')
    """

    plt.title('d_length={0}, d_top_bit={1}, d_weight={2}, {3}, LOOP={4}'.format(d_length, d_top_bit, d_weight, title, loop_times))
    plt.xlabel('count')
    plt.ylabel('frequency')
    plt.legend(loc = 'upper left')
    plt.show()

def frequency(list):

    # countの最大数を探索する.
    max = -1
    for item in list:
        if max <= item:
            max = item

    # 0から(max+3)までの数字を順にcount_listに格納する(要はグラフのx軸となる).
    freq_list = [0] * (max+3)
    count_list = []
    k = 0
    for item in freq_list:
        count_list.append(k)
        k += 1

    # freq_listに頻度を格納する.
    for item in list:
        freq_list[item] += 1

    return count_list, freq_list
