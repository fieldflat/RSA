#
# バイナリ法を実行するプログラム
#

import math
import main


p = main.p
q = main.q
N = main.N
phi_N = main.phi_N

#
# バイナリ法
# c, dを入力として, m = c**d mod N を返す
#
def binary_method(c, d, N):
    print('*************binary_method*************')

    count = 0
    m = c
    array_d = binary_d(d)
    l = len(array_d)
    for i in range(1, l):
        #m = (m ** 2) % N
        m, count = modulo(m**2, N, count)
        if array_d[i] == 1:
            #m = (m*c) % N
            count += 1
            m, count = modulo(m*c, N, count)
    return m, count

#
# x mod yの値を, %演算子を使わずに計算する.
# 余分な計算をした場合はcountを1インクリメントする.
#
def modulo(x, y, count):

    if x > y:
        count += 1
        x = x % y

    """
    while x > y:
        count += 1
        x -= y
    """
    return x, count

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
