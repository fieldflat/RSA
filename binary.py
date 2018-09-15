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
# 剰余演算の回数mod_count, 乗算演算の回数mult_countも返す.
#
def binary_method(c, d, N):

    mod_count = 0 # 剰余計算のカウント
    mult_count = 0 # 乗算計算のカウント
    m = c
    array_d = binary_d(d) # 鍵dを2進表現にしてリストに格納する
    l = len(array_d) # 2進表現の長さを獲得.
    for i in range(1, l):
        #m = (m ** 2) % N
        mult_count += 1 # mを二乗するため
        m, mod_count = modulo(m**2, N, mod_count)
        if array_d[i] == 1:
            #m = (m*c) % N
            mult_count += 1 # m*cを実行するため
            m, mod_count = modulo(m*c, N, mod_count)
    return m, mod_count, mult_count

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
