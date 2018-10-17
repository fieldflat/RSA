#
# バイナリ法を実行するプログラム
#

import math
import main


p = main.p
q = main.q
N = main.N
phi_N = main.phi_N

flag = 100

#
# バイナリ法
# c, dを入力として, m = c**d mod N を返す
# 剰余演算の回数mod_count, 乗算演算の回数mult_countも返す.
#
def binary_method(c, d, N):

    #print('~~~~~~~~~~~~~ binary_method({0}, {1}, {2}) ~~~~~~~~~~~~~~~~~'.format(c, d, N))
    mod_count = 0 # 剰余計算のカウント
    mult_count = 0 # 乗算計算のカウント
    m = c
    array_d = binary_d(d) # 鍵dを2進表現にしてリストに格納する
    #print('array_d = {0}'.format(array_d))
    l = len(array_d) # 2進表現の長さを獲得.
    #print('length(array_d) = {0}'.format(l))
    for i in range(1, l):
        #m = (m ** 2) % N
        m, mult_count = multiply(m, m, mult_count) # m = m*mの実行
        m, mod_count = modulo(m, N, mod_count) # m % Nの実行
        if array_d[i] == 1:
            #m = (m*c) % N
            m, mult_count = multiply(m, c, mult_count) # m = m*cの実行
            m, mod_count = modulo(m, N, mod_count) # m % Nの実行
    return m, mod_count, mult_count

#
# x mod yの値を計算する.
# x > yの場合はmod_countを1インクリメントする.
#
def modulo(x, y, mod_count):

    """
    質問その1：この条件分岐は必要かどうか？
    """
    #print('modulo({0}, {1}, {2}) = '.format(x, y, mod_count))
    if (x > y) or (x < 0):
        mod_count += 1
        x = x % y
    else:
        print('countしなかったよ*******************************************************')
    #print('{0}, {1}'.format(x, mod_count))
    return x, mod_count

#
# x * yの値を計算し, mult_countの値を
# インクリメントしてそれぞれ返す.
#
def multiply(x, y, mult_count):

    global flag
    #print(flag)
    #print('multiply({0}, {1}, {2}) = '.format(x, y, mult_count) )
    mult_count += 1
    ans = x * y


    if (x == y):
        flag = 1
        #print('**********************  flag = {0}'.format(flag))
    else:
        flag = 0

    """
    if (x != y) and (ans >= N):
        print('1')
    elif (x != y) and (ans < N):
        print('0')
    """

    #print('{0}, {1}'.format(ans, mult_count))
    return ans, mult_count


#
# 10進数dを2進数に変換し, 配列として返す.
#
def binary_d(d):
    array_d = []
    while(1):
        array_d.append(d % 2)
        d = d // 2
        if(d == 0):
            break
    array_d.reverse()
    return array_d


def average(list):
    sum = 0
    for num in list:
        sum += num

    m = sum / len(list)

    print("平均：{0}".format(m))
